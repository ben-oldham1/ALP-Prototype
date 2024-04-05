// Function to query the AI and display the response
const sendMessage = async () => {
    const chatArea = document.getElementById('chat-area');
    const message = document.getElementById('user-message').value;

    var codeContents = editor.getValue();

    function outputMsg(chatArea, user, message) {
        // Showdown js for markdown to HTML conversion
        var converter = new showdown.Converter();
        var htmlMessage = converter.makeHtml(message);

        const messageElement = document.createElement('div');
        messageElement.className = "row mb-2";
        messageElement.innerHTML = `<div class="col-12"><strong>${user}</strong></div>
                                    <div class="col-12">${htmlMessage}</div>`;
        chatArea.appendChild(messageElement);
    }

    function createLoadingAnimation() {
        const loadingElement = document.createElement('div');
        loadingElement.className = "d-flex align-items-center gap-3";
        loadingElement.id = "loading-animation";
        loadingElement.innerHTML = `<div class="spinner-grow text-body-tertiary" role="status" aria-hidden="true"></div>
                                    AI thinking...`;
        return loadingElement;
    }

    // Display the original query
    outputMsg(chatArea, 'You', message);

    // Create and append the loading animation
    const loadingAnimation = createLoadingAnimation();
    chatArea.appendChild(loadingAnimation);

    // Make the request to server
    const response = await fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            message: message,
            codeContents: codeContents
        })
    });

    const data = await response.json();
    const chatbotResponse = data.response['response'];

    // Remove the loading animation
    document.getElementById('loading-animation').remove();

    // Display the response
    outputMsg(chatArea, 'ByteLearn', chatbotResponse);

    // Add a dividing line
    const divider = document.createElement('hr');
    chatArea.appendChild(divider);
}

const clearChat = () => {
    document.getElementById('chat-area').innerHTML = '';
}