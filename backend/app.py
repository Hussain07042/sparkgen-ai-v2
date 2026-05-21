import os
import gradio as gr

# Simple AI-style chatbot logic (safe fallback working version)
def respond(message, history):
    message = message.lower()

    if "sad" in message or "angry" in message:
        return "I understand how you feel. I'm here with you ❤️"
    elif "happy" in message:
        return "That’s great! Keep smiling 😊"
    elif "love" in message:
        return "Love is a beautiful feeling 💙"
    elif "hello" in message:
        return "Hello! I am SparkGen AI 🤖"
    else:
        return f"You said: {message}"

# Gradio UI
demo = gr.ChatInterface(
    fn=respond,
    title="SparkGen AI V2",
    description="Simple working AI chat (Railway safe)"
)

# IMPORTANT: Railway PORT FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    import os

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)
    )
