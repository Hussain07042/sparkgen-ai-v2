from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import gradio as gr

app = FastAPI()

def chat(message):
    return f"🤖 SparkGen AI: You said -> {message}"

demo = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="SparkGen AI V2",
    description="Simple working AI chat (Railway safe version)"
)

# Mount Gradio on FastAPI
app = gr.mount_gradio_app(app, demo, path="/")

@app.get("/health", response_class=HTMLResponse)
def health():
    return "<h1>✅ SparkGen AI is running</h1>"
