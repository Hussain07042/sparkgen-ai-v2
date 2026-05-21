const API = "http://127.0.0.1:8000";


// ================= CHAT =================
async function chat() {

    let text = document.getElementById("chatInput").value;
    let lang = document.getElementById("langSelect").value;

    let res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text, lang })
    });

    let data = await res.json();

    document.getElementById("chatResult").innerHTML +=
        `<div class="bot">🤖 ${data.reply}</div>`;
}


// ================= EMOTION =================
async function emotion() {

    let text = document.getElementById("emotionInput").value;

    if (!text) return;

    let res = await fetch(`${API}/emotion`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    let data = await res.json();

    document.getElementById("emotionResult").innerText =
        "Emotion: " + data.emotion;
}


// ================= SENTIMENT =================
async function predict() {

    let text = document.getElementById("sentimentInput").value;

    if (!text) return;

    let res = await fetch(`${API}/predict`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    let data = await res.json();

    let result = data.prediction[0];

    document.getElementById("sentimentResult").innerText =
        `${result.label} (${result.score.toFixed(2)})`;
}