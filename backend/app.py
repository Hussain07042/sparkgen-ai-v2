import os
import gradio as gr

# Simple AI Chat (NO API KEYS NEEDED - SAFE DEMO VERSION)

def chat(message, history):
    message = message.lower()

    if "hello" in message:
        return "Hello 👋 I'm SparkGen AI. How can I help you today?"

    elif "sad" in message or "not happy" in message:
        return "I'm sorry you're feeling that way 😔. I'm here for you."

    elif "happy" in message:
        return "That's great 😊 Keep smiling!"

    elif "ai" in message:
        return "AI means Artificial Intelligence — like me 🤖"

    elif "bye" in message:
        return "Goodbye 👋 Take care!"

    else:
        return "I am SparkGen AI V2 🤖 I can chat, motivate you, and answer simple questions."

demo = gr.ChatInterface(fn=chat, title="SparkGen AI V2")

if __name__ == "__main__":
    demo.launch()
