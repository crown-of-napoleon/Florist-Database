const express = require("express");
const Note = require("../models/model");
const redis = require("../redisClient");

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
    next(); // Continue to the next middleware or route handler
  }
};

// POST is used to save the current entry
router.post("/", async (req, res) => {
  try {
    const { title, price, quantity, content } = req.body;
    const note = new Note({ title, price, quantity, content });
    await note.save();
    await redis.del('notes'); // Invalidate cache
    res.status(201).json(note);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// GET is used to retrieve the entries in the database
router.get("/", cacheMiddleware, async (req, res) => {
  try {
    const notes = await Note.find({});
    await redis.set('notes', JSON.stringify(notes), 'EX', 3600); // Cache for 1 hour
    res.status(200).json(notes);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// DELETE is used to delete a specific entry
router.delete("/:id", async (req, res) => {
  try {
    const note = await Note.findByIdAndDelete(req.params.id);
    if (!note) {
      return res.status(404).json({ error: "Note not found" });
    }
    await redis.del('notes'); // Invalidate cache
    res.status(200).json(note);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Update an entry, used to change the quantity
router.patch("/:id", async (req, res) => {
  try {
    const { quantity, content } = req.body;
    const updates = {};
    if (quantity !== undefined) {
      updates.quantity = quantity;
    }
    if (content !== undefined) {
      updates.content = content;
    }
    const note = await Note.findByIdAndUpdate(req.params.id, updates, { new: true });
    if (!note) {
      return res.status(404).json({ error: "Note not found" });
    }
    await redis.del('notes'); // Invalidate cache
    res.status(200).json(note);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;