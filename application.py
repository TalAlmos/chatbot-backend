from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv
from knowledge_base import CLINIC_INFO

# Load environment variables
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Please check your .env file.")

# Initialize FastAPI
app = FastAPI()
client = OpenAI(api_key=api_key)

# Setup templates and static files
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    conversation_history: list[dict] = []

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Create system message using knowledge base
        system_message = f"""You are Dr. Almos' clinic assistant. You must ONLY provide information that is contained in the following knowledge base:

        טיפולים זמינים:
        {CLINIC_INFO['treatments']}

        תהליך קביעת תורים:
        {CLINIC_INFO['booking']}

        מידע לאחר טיפול:
        {CLINIC_INFO['post_treatment']}

        מיקום ופרטי התקשרות:
        {CLINIC_INFO['location']}

        מידע על ד"ר אלמוס:
        {CLINIC_INFO['doctor']}

        Important rules:
        1. Respond ONLY in Hebrew
        2. Only use information from the knowledge base above
        3. If information is not in the knowledge base, say: "מצטער, אין לי מידע זמין על כך. אנא צור קשר עם המרפאה ישירות."
        4. Keep responses clear and professional
        """

        # Prepare messages
        messages = [{"role": "system", "content": system_message}]
        messages.extend([{"role": msg["role"], "content": msg["content"]} 
                        for msg in request.conversation_history])
        messages.append({"role": "user", "content": request.message})

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=250,
            temperature=0.3,
            presence_penalty=-0.5,
            frequency_penalty=0.0
        )

        return JSONResponse({
            "response": response.choices[0].message.content,
            "status": "success"
        })

    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e),
                "type": type(e).__name__
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
