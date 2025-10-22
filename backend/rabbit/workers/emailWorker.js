// backend/workers/emailWorker.js
const amqp = require("amqplib");
const nodemailer = require("nodemailer");
const queueName = "email_updates";
const path = require("path");
// Find the .env file in the root directory (up two levels from workers)
require("dotenv").config({
    path: path.resolve(__dirname, '../../.env') 
});

async function startWorker() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();
  await channel.assertQueue(queueName, { durable: true });
  
  console.log("✅ Email worker connected to RabbitMQ");

  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS,
    },
  });

  channel.consume(queueName, async (msg) => {
    const data = JSON.parse(msg.content.toString());
    console.log("📨 Received message:", data);

    try {
      let subject, text;
      
      switch(data.action) {
        case 'created':
          subject = `New Inventory Item: ${data.title}`;
          text = `A new item "${data.title}" has been added.\nQuantity: ${data.quantity}\nPrice: $${data.price}`;
          break;
        case 'updated':
          subject = `Inventory Update: ${data.title}`;
          text = `The item "${data.title}" has been updated.\nNew Quantity: ${data.quantity}\nPrice: $${data.price}`;
          break;
        case 'deleted':
          subject = `Inventory Item Removed: ${data.title}`;
          text = `The item "${data.title}" has been removed from inventory.`;
          break;
        default:
          subject = `Inventory Notification: ${data.title}`;
          text = `Update for "${data.title}": Quantity ${data.quantity}`;
      }

      const mailOptions = {
        from: `"Florist Database" <${process.env.EMAIL_USER}>`,
        to: process.env.NOTIFY_TO,
        subject: subject,
        text: text,
      };

      await transporter.sendMail(mailOptions);
      console.log("✅ Email sent successfully");
      channel.ack(msg);
    } catch (err) {
      console.error("❌ Failed to send email:", err);
      channel.nack(msg, false, false);
    }
  });
}

startWorker().catch(console.error);