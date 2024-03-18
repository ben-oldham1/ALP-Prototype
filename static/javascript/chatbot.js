// Function to query the AI and display the response
const sendMessage = async () => {

    // Get the div that will hold the request and response text
    const chatArea = document.getElementById('chat-area');

    // Get the user query text
    const message = document.getElementById('user-message').value;

    // Function to format the output message
    // Takes chatArea object, name of user (You or AI) and the message to display
    function outputMsg(chatArea, user, message) {
        return chatArea.innerHTML += `<div class="row mb-2">
    <div class="col-12"><strong>${user}</strong></div>
    <div class="col-12"><pre>${message}</pre></div>
    </div>`;
    }

    // Display the original query
    outputMsg(chatArea, 'You', message);

    // Make the request to server
    const response = await fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    });

    // Save the AI response from server
    const data = await response.json();
    const chatbotResponse = data.response['response'];

    // Display the response
    outputMsg(chatArea, 'ByteLearn', chatbotResponse);

    // Add a dividing line
    chatArea.innerHTML += '<hr>';
}

const clearChat = () => {
    document.getElementById('chat-area').innerHTML = '';
}