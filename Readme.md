# AI Interview Chat Bot

An AI-powered Interview Question Generator built using Streamlit, FastAPI, and Groq LLM (LLaMA 3.3).

---

# Project Overview

This project helps users generate **interview questions and answers** based on topic and difficulty level.

Users can:

- Generate interview questions
- Select difficulty level (Easy / Medium / Hard)
- Choose question type (MCQ / Theory / Coding)
- Get AI-generated answers
- View results in an interactive UI

---

# Technologies Used

| Technology | Purpose |
|------|------|
| Python | Programming Language |
| Streamlit | Frontend UI |
| FastAPI | Backend API |
| Groq LLM (LLaMA 3.3) | AI Model |
| Requests | API Communication |
| Uvicorn | ASGI Server |

---

# Project Structure

```text
AI-Interview-ChatBot/
│
├── frontend/
│   └── app.py
│
├── backend/
│   └── main.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# Frontend Explanation

The frontend is built using Streamlit.

## Frontend Features

- Enter topic for interview
- Select difficulty level
- Choose question type
- Generate AI interview questions
- Expand and view Q&A

## Streamlit Components Used

| Component | Purpose |
|------|------|
| st.title() | Page Title |
| st.text_input() | Input Topic |
| st.selectbox() | Select Difficulty |
| st.multiselect() | Select Question Type |
| st.form_submit_button() | Submit Form |
| st.expander() | Show Q&A Expandable View |
| st.write() | Display Output |

---

# Backend Explanation

The backend is built using FastAPI and Groq API.

## Backend Features

- API endpoint for question generation
- Integration with Groq LLM
- Prompt handling
- Response formatting

---

# API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| POST | /generate | Generate Interview Questions |

---

# API Flow

```text
User Input
   ↓
Streamlit Frontend
   ↓ POST Request
FastAPI Backend
   ↓ Prompt sent to Groq LLM
AI Model Response
   ↓
JSON Output Returned
   ↓
Streamlit Displays Q&A
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone <repository_link>
cd AI-Interview-ChatBot
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements.txt

```txt
streamlit
fastapi
uvicorn
openai
requests
```

---

# Environment Variables (.env)

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# Run Backend Server

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# Run Frontend Application

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# Project Workflow

```text
User Input
   ↓
Streamlit UI
   ↓
FastAPI Backend
   ↓
Groq LLM (AI Model)
   ↓
JSON Response
   ↓
Streamlit Display (Q&A)
```

---

# Advantages

- Easy Interview Preparation
- AI-powered learning
- Fast response system
- Beginner-friendly UI

---

# Future Enhancements

- MCQ scoring system
- Timer-based interview mode
- Resume-based question generation
- Save interview history
- Voice-based interview assistant

---

# Author

Sampath Kumar

---

# License

This project is for educational purposes only.
```