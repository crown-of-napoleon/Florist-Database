// backend/rabbit.js
const amqp = require("amqplib");

let channel, connection;
const queueName = "email_updates";

async function connectQueue() {
  connection = await amqp.connect("amqp://localhost");
  channel = await connection.createChannel();
  await channel.assertQueue(queueName, { durable: true });
  console.log("✅ Connected to RabbitMQ and queue initialized");
}

function sendToQueue(message) {
  if (!channel) throw new Error("RabbitMQ channel not initialized");
  channel.sendToQueue(queueName, Buffer.from(JSON.stringify(message)), { persistent: true });
  console.log("📤 Message sent to queue:", message);
}

module.exports = { connectQueue, sendToQueue };
