class ChatInterface {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.chatForm = document.getElementById('chatForm');
        this.userInput = document.getElementById('userInput');
        this.conversationHistory = [];
        this.conversationStarters = document.getElementById('conversationStarters');
        
        this.initializeEventListeners();
        this.initializeConversationStarters();
        const resetButton = document.getElementById('resetChat');
        if (resetButton) {
            resetButton.addEventListener('click', () => this.resetConversation());
        }
    }

    initializeEventListeners() {
        this.chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleUserMessage();
        });
    }

    initializeConversationStarters() {
        const buttons = document.querySelectorAll('.starter-button');
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const message = button.dataset.message;
                this.handleStarterClick(message);
            });
        });
    }

    handleStarterClick(message) {
        // Hide conversation starters after selection
        this.conversationStarters.style.display = 'none';
        
        // Process the message
        this.userInput.value = message;
        this.handleUserMessage();
    }

    async handleUserMessage() {
        const message = this.userInput.value.trim();
        if (!message) return;

        // Clear input
        this.userInput.value = '';

        // Add user message to chat
        this.addMessage(message, 'user');

        try {
            const response = await this.sendMessageToBackend(message);
            this.addMessage(response.response, 'bot');
        } catch (error) {
            this.addMessage('מצטער, אירעה שגיאה. אנא נסה שוב.', 'bot error');
            console.error('Error:', error);
        }
    }

    async sendMessageToBackend(message) {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                conversation_history: this.conversationHistory
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;

        messageDiv.appendChild(messageContent);
        this.chatMessages.appendChild(messageDiv);

        // Store in conversation history
        this.conversationHistory.push({
            role: type === 'user' ? 'user' : 'assistant',
            content: content
        });

        // Scroll to bottom
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    resetConversation() {
        this.conversationHistory = [];
        this.chatMessages.innerHTML = '';
        this.conversationStarters.style.display = 'flex';
    }
}

// Initialize chat interface when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ChatInterface();
});