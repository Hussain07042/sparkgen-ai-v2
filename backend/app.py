import os
import gradio as gr
from huggingface_hub import InferenceClient

# Get token from Railway Secrets / Environment Variables
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

def chat(message, history):
    messages = []

    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})

    messages.append({"role": "user", "content": message})

    response = client.chat_completion(
        messages,
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
    )

    return response.choices[0].message.content


demo = gr.ChatInterface(
    fn=chat,
    title="🔥 SparkGen AI v2",
    description="Your AI chatbot is running on Hugging Face + Railway"
)

if __name__ == "__main__":
    demo.launch()
