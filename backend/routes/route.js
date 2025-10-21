const express = require("express");
const Note = require("../models/model");
const redis = require("../redisClient");
const { sendToQueue } = require("../rabbit/rabbit.js"); // Import the producer function
const router = express.Router();

// Cache middleware
const cacheMiddleware = async (req, res, next) => {
  try {
    const cachedData = await redis.get('notes');
    if (cachedData) {
      return res.status(200).json(JSON.parse(cachedData));
    }
    next();
  } catch (error) {
    console.error('Redis error:', error);
    next();
  }
};

// POST - Create new entry and send notification
router.post("/", async (req, res) => {
  try {
    const { title, price, quantity, content } = req.body;
    const note = new Note({ title, price, quantity, content });
    await note.save();
    await redis.del('notes'); // Invalidate cache
    
    // Send message to RabbitMQ queue
    sendToQueue({
      action: 'created',
      title: note.title,
      quantity: note.quantity,
      price: note.price,
      id: note._id
    });
    
    res.status(201).json(note);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// GET - Retrieve entries
router.get("/", cacheMiddleware, async (req, res) => {
  try {
    const notes = await Note.find({});
    await redis.set('notes', JSON.stringify(notes), 'EX', 3600);
    res.status(200).json(notes);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// DELETE - Remove entry and send notification
router.delete("/:id", async (req, res) => {
  try {
    const note = await Note.findByIdAndDelete(req.params.id);
    if (!note) {
      return res.status(404).json({ error: "Note not found" });
    }
    await redis.del('notes');
    
    // Send deletion notification to queue
    sendToQueue({
      action: 'deleted',
      title: note.title,
      quantity: 0,
      id: note._id
    });
    
    res.status(200).json(note);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// PATCH - Update entry and send notification
router.patch("/:id", async (req, res) => {
  try {
    const { quantity, content, price } = req.body;
    const updates = {};
    
    if (quantity !== undefined) updates.quantity = quantity;
    if (content !== undefined) updates.content = content;
    if (price !== undefined) updates.price = price;
    
    const note = await Note.findByIdAndUpdate(req.params.id, updates, { new: true });
    
    if (!note) {
      return res.status(404).json({ error: "Note not found" });
    }
    
    await redis.del('notes');
    
    // Send update notification to queue
    sendToQueue({
      action: 'updated',
      title: note.title,
      quantity: note.quantity,
      price: note.price,
      id: note._id
    });
    
    res.status(200).json(note);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;