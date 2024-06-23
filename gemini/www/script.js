
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    document.getElementById('user-input').value = '';
    const chatbox = document.getElementById('chatbox');
    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message');
    userMessage.textContent = userInput;
    chatbox.appendChild(userMessage);

    const botResponse = await eel.chat_with_bot(userInput)();
    const botMessage = document.createElement('div');
    botMessage.classList.add('bot-message');
    botMessage.textContent = "bot: "+botResponse;
    chatbox.appendChild(botMessage);

    chatbox.scrollTop = chatbox.scrollHeight;
}

document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});