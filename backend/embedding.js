require("dotenv").config();
const { GoogleGenerativeAI } = require("@google/generative-ai");
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function getGeminiEmbedding(text) {
  const model = genAI.getGenerativeModel({ model: "text-embedding-004" }); 
  const result = await model.embedContent(text);
  return result.embedding.values;
}

module.exports = { getGeminiEmbedding };
