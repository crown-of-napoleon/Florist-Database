const mongoose = require("mongoose");

const NoteSchema = new mongoose.Schema({
  title: { type: String, required: true },
  price: { type: Number, required: true},
  content: { type: String, required: false },
});

const Note = mongoose.model("Note", NoteSchema);
module.exports = Note;
