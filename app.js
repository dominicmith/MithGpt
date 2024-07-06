document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('user-input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});

let currentAudio = null;
function sendMessage() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput === "") return;

    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="message user">${userInput}</div>`;
    document.getElementById('user-input').value = "";

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            const audioPath = data.audio;
            chatBox.innerHTML += `<div class="message bot">${botResponse}</div>`;

            if (currentAudio) {
                currentAudio.pause();
                currentAudio.currentTime = 0;
            }

            currentAudio = new Audio(audioPath);
            currentAudio.play();

            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => console.error('Error fetching response:', error));
}
