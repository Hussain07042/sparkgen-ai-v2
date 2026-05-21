function sendMessage() {
  let input = document.getElementById("input");
  let chat = document.getElementById("chat");

  let userText = input.value;
  if (!userText) return;

  chat.innerHTML += "<p><b>You:</b> " + userText + "</p>";

  let response = getAIResponse(userText);

  chat.innerHTML += "<p><b>AI:</b> " + response + "</p>";

  input.value = "";
  chat.scrollTop = chat.scrollHeight;
}

function getAIResponse(text) {
  text = text.toLowerCase();

  if (text.includes("hello")) {
    return "Hello 👋 I am SparkGen AI V2";
  }
  if (text.includes("sad")) {
    return "I'm here for you ❤️";
  }
  if (text.includes("happy")) {
    return "That's amazing 😄";
  }
  if (text.includes("ai")) {
    return "AI means machines that simulate human intelligence 🤖";
  }

  return "I don't understand yet, but I'm learning 🤖";
}
