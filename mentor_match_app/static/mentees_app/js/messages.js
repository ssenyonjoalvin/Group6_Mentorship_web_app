document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.list-group-item');
    const chatContent = document.getElementById('chat-content');

    messages.forEach(message => {
        message.addEventListener('click', function(e) {
            e.preventDefault();
            const chatId = this.getAttribute('data-chat-id');

            // Fetch chat details
            fetch(`/api/chats/${chatId}/`)  // Adjust the endpoint as needed
                .then(response => response.json())
                .then(data => {
                    // Update chat content
                    chatContent.innerHTML = `
                        <h4>Chat with ${data.mentor.name}</h4>
                        <div>
                            ${data.messages.map(msg => `
                                <div class="message">
                                    <p><strong>${msg.sender}</strong>: ${msg.text}</p>
                                    <small class="text-muted">${msg.time}</small>
                                </div>
                            `).join('')}
                        </div>
                        <form id="send-message-form">
                            <textarea class="form-control" placeholder="Type your message here..."></textarea>
                            <button type="submit" class="btn btn-primary mt-2">Send</button>
                        </form>
                    `;
                })
                .catch(error => {
                    console.error('Error fetching chat details:', error);
                    chatContent.innerHTML = '<p class="text-danger">Failed to load chat details.</p>';
                });
        });
    });
});
