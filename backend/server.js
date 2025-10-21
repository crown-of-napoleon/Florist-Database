const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const { connectQueue } = require("./rabbit"); // Add this import
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json()); // To parse JSON bodies

// Connect to the database
const PORT = process.env.PORT || 5000; // Fixed: was 500, should be 5000

mongoose
  .connect(process.env.MONGODB_URI)
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Initialize RabbitMQ connection
connectQueue().catch((err) => {
  console.error("Failed to connect to RabbitMQ:", err);
});

// Define routes specified in the route.js file
const notesRouter = require("./routes/route.js");
app.use("/api/notes", notesRouter);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});