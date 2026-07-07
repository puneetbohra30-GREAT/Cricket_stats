import React, { useState } from "react";
import { sendChat } from "../api/apiService";

function ChatBot() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMsg = { type: "user", text: message };
    setMessages((prev) => [...prev, userMsg]);

    setLoading(true);

    try {
      const res = await sendChat(message);

      let replyText = "No response";

      if (res) {
        if (typeof res === "string") {
          replyText = res;
        } else if (res.response) {
          replyText = res.response;   //  main fix
        } else if (res.reply) {
          replyText = res.reply;
        } else if (res.message) {
          replyText = res.message;
        } else if (res.data) {
          replyText = JSON.stringify(res.data);
        }
      }

      const botMsg = {
        type: "bot",
        text: replyText,
      };

      setMessages((prev) => [...prev, botMsg]);

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "Server error " },
      ]);
    }

    setLoading(false);
    setMessage("");
  };

  return (
    <div>
      <h2>🤖 AI Chat</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          minHeight: "200px",
          marginBottom: "10px",
          overflowY: "auto",
        }}
      >
        {messages.length === 0 && <p>Start chatting...</p>}

        {messages.map((msg, i) => (
          <p key={i}>
            <b>{msg.type === "user" ? "You" : "Bot"}:</b> {msg.text}
          </p>
        ))}

        {loading && <p>Bot is typing...</p>}
      </div>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />

      <button onClick={handleSend} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>
    </div>
  );
}

export default ChatBot;
