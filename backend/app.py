import gradio as gr

# Simple AI-style chatbot (safe fallback, no API needed)
def chat(message, history):
    history = history or []

    response = f"🤖 SparkGen AI: I received your message -> {message}"

    history.append((message, response))
    return history, history

with gr.Blocks(title="SparkGen AI V2") as demo:
    gr.Markdown("# 🤖 SparkGen AI V2")
    gr.Markdown("Simple working AI chat (Railway deployment safe)")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message")

    state = gr.State([])

    msg.submit(chat, inputs=[msg, state], outputs=[chatbot, state])

demo.launch(
    server_name="0.0.0.0",
    server_port=7860
)
