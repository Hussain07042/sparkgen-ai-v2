from transformers import pipeline

# Sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Emotion (lightweight rule-based)
def detect_emotion(text: str):
    text = text.lower()

    if any(x in text for x in ["happy", "love", "great", "excited"]):
        return "happy 😄"
    elif any(x in text for x in ["angry", "mad", "hate"]):
        return "angry 😡"
    elif any(x in text for x in ["sad", "cry", "depressed"]):
        return "sad 😢"
    elif any(x in text for x in ["fear", "scared"]):
        return "fear 😨"
    else:
        return "neutral 😐"


# Chat system
def chat_response(text: str):
    text = text.lower()

    if "hello" in text:
        return "Hello! I am SparkGen AI 🤖"

    elif "name" in text:
        return "I am SparkGen AI built by Hussain Adam Umar 🚀"

    elif "help" in text:
        return "I can help with AI predictions, emotion detection, and chat!"

    else:
        return "I understand your message."