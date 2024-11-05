const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json()); // To parse JSON bodies

// Connect the the databse
const PORT = process.env.PORT || 500;
mongoose
  .connect(process.env.MONGODB_URI)
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Define routes specified in the route.js file
const notesRouter = require("./routes/route.js");
app.use("/api/notes", notesRouter);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
