// Mongoose is used to connect to the MongoDB database
const mongoose = require("mongoose");

// The schema is as follows:
// title: The title of the entry (a flower)
// price: price of that flower
// quantity: amount of that type of flower available in the inventory
// content: description of this entry (brief information)
const NoteSchema = new mongoose.Schema({
  title: { type: String, required: true },
  price: { type: Number, required: true},
  quantity: {type: Number, required: true},
  content: { type: String, required: false },
  embedding: {
    type: [Number],
    index: "vector", // Marks this as a vector index field
    dimensions: 768, // Gemini text-embedding-004 outputs 768-dimensional vectors
    similarity: "cosine", // Use cosine similarity for vector search
  },
});

// Create this model according to to schema defined above
const Note = mongoose.model("Note", NoteSchema);
module.exports = Note;
