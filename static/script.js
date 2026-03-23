const chatBox = document.getElementById('chat-box');
const inputField = document.getElementById('message-input');
const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
const wsUrl = `${wsProtocol}//${window.location.host}/ws/chat`;
let socket;

function connect() {
    socket = new WebSocket(wsUrl);

    socket.onopen = function() {
        console.log("Connected to WebSocket");
        addMessage("System", "Connected to global support server.", "system");
    };

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        // data contains: response, detected_lang
        addMessage("Bot", data.response, "bot", data.detected_lang);
    };

    socket.onclose = function() {
        console.log("Disconnected. Reconnecting...");
        setTimeout(connect, 3000);
    };

    socket.onerror = function(error) {
        console.error("WebSocket Error: " + error);
    };
}

function sendMessage() {
    const message = inputField.value.trim();
    if (message && socket.readyState === WebSocket.OPEN) {
        socket.send(message);
        addMessage("You", message, "user");
        inputField.value = '';
    }
}

function addMessage(sender, text, type, lang=null) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message');
    msgDiv.classList.add(type === 'user' ? 'user-message' : 'bot-message');
    
    let content = `<div>${text}</div>`;
    if (lang && type === 'bot') {
        content += `<span class="meta-info">Detected: ${lang} | Translated</span>`;
    }
    
    msgDiv.innerHTML = content;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

inputField.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// Start connection
connect();
