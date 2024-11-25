# Dr. Almos Clinic Chatbot

A responsive, multilingual chatbot designed specifically for Dr. Almos' medical clinic. The chatbot provides instant responses to patient inquiries about treatments, booking procedures, and clinic information in Hebrew.

## 🌟 Features

- **Real-time Chat Interface**: Instant responses to patient queries
- **Mobile-Responsive Design**: Seamless experience across all devices
- **Hebrew Language Support**: Fully supports RTL and Hebrew text
- **Knowledge Base Integration**: Accurate responses based on clinic-specific information
- **Conversation History**: Maintains context throughout the chat session
- **Easy Website Integration**: Can be embedded into existing websites

## 🔧 Technical Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: OpenAI GPT-3.5 Turbo
- **Database**: None (Stateless)

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Node.js (for development)

## 🚀 Installation

1. **Clone the repository**
2. **Set up virtual environment**
3. **Install dependencies**
4. **Configure environment variables**
Create a `.env` file in the root directory:
5. **Run the application**

The server will start at `http://localhost:8000`

## 💻 Usage

### Standalone Web Application
Access the chatbot directly through the web interface at `http://localhost:8000`

### Website Integration
Add the following code to your website:

html
<!-- Add in the <head> section -->
<link rel="stylesheet" href="path/to/chat-widget.css">
<!-- Add just before closing </body> tag -->
<script src="path/to/chat-widget.js"></script>
<script>
document.addEventListener('DOMContentLoaded', () => {
const chatWidget = new ChatWidget();
});
</script>

## 📁 Project Structure
dr-almos-chatbot/
├── application.py # Main FastAPI application
├── knowledge_base.py # Clinic information and responses
├── requirements.txt # Python dependencies
├── static/
│ ├── css/
│ │ └── chat-widget.css
│ ├── js/
│ │ └── chat-widget.js
│ └── images/
├── templates/
│ └── index.html
└── .env # Environment variables (not in repo)


## ⚙️ Configuration

The chatbot can be configured through the following files:
- `knowledge_base.py`: Update clinic information and responses
- `static/css/chat-widget.css`: Customize the appearance
- `application.py`: Modify API settings and response parameters

## 🔒 Security

- CORS middleware configured for secure cross-origin requests
- Environment variables for sensitive data
- Rate limiting on API endpoints
- Input validation using Pydantic models

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGithub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Dr. Almos' Clinic for providing the knowledge base
- OpenAI for the GPT-3.5 API
- FastAPI community for the excellent framework

## 📞 Support

For support, email tal.almos@gmail.com or open an issue in the repository.
