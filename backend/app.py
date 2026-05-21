import gradio as gr

def chat(message):
    return f"🤖 SparkGen AI: You said -> {message}"

demo = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="SparkGen AI V2",
    description="Simple working AI chat (Railway safe version)"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=8000
    )
