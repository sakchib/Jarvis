document.getElementById('sendBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    document.getElementById('response').innerText = `You asked: ${userInput}`;
    // Yahan aap Jarvis ka backend API call kar sakte hain
});
