import gradio as gr
from huggingface_hub import InferenceClient
import os

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    token=HF_TOKEN,
    model="mistralai/Mistral-7B-Instruct-v0.2"
)

def chat(message, history):
    messages = []

    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})

    messages.append({"role": "user", "content": message})

    response = client.chat_completion(
        messages,
        max_tokens=200,
        temperature=0.7
    )

    return response.choices[0].message["content"]

demo = gr.ChatInterface(fn=chat, title="SparkGen AI v2 🤖")

demo.launch(server_name="0.0.0.0", server_port=7860)
