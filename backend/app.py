from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AI MODEL
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


class TextInput(BaseModel):
    text: str
class TextInput(BaseModel):
    text: str
    lang: str = "en"


@app.get("/")
def home():
    return {"message": "SparkGen AI v2 is running"}


@app.post("/predict")
def predict(data: TextInput):

    result = sentiment_model(data.text)

    return {
        "input": data.text,
        "prediction": result
    }


@app.post("/emotion")
def emotion(data: TextInput):

    text = data.text.lower()

    if any(x in text for x in ["happy", "love", "great"]):
        emotion = "happy 😄"

    elif any(x in text for x in ["angry", "mad"]):
        emotion = "angry 😡"

    elif any(x in text for x in ["sad", "cry"]):
        emotion = "sad 😢"

    elif any(x in text for x in ["fear", "scared"]):
        emotion = "fear 😨"

    else:
        emotion = "neutral 😐"

    return {
        "text": data.text,
        "emotion": emotion
    }


@app.post("/chat")
def chat(data: TextInput):

    text = data.text.lower()
    lang = data.lang

    # ENGLISH RESPONSES
    if lang == "en":

        if "hello" in text:
            reply = "Hello! I am SparkGen AI 🤖"

        elif "name" in text:
            reply = "I am SparkGen AI built by Hussain Adam Umar 🚀"

        elif "happy" in text:
            reply = "That is wonderful to hear 😄"

        elif "sad" in text:
            reply = "I hope things get better soon 💙"

        else:
            reply = f"You said: {data.text}"

    # HAUSA RESPONSES
    else:

        if "hello" in text:
            reply = "Sannu! Ni SparkGen AI ne 🤖"

        elif "name" in text:
            reply = "Ni SparkGen AI wanda Hussain Adam Umar ya gina 🚀"

        elif "happy" in text:
            reply = "Muna farin ciki da jin haka 😄"

        elif "sad" in text:
            reply = "Ina fatan abubuwa za su gyaru 💙"

        else:
            reply = f"Kayi cewa: {data.text}"

    return {
        "input": data.text,
        "reply": reply,
        "language": lang
    }


@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>SparkGen AI v2</title>
    </head>
    <body style="text-align:center;font-family:Arial;margin-top:100px;">
    <h1>🚀 SparkGen AI v2</h1>
    <p>Your AI is working successfully</p>
    </body>
    </html>
    """