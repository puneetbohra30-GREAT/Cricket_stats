# 🏏 Cricket Stats AI

Cricket Stats AI is a full-stack web application built to provide real-time cricket data, player analytics, and AI-powered insights. It combines a modern React frontend with a FastAPI backend to deliver a scalable and intelligent sports analytics platform.

This project demonstrates strong skills in full-stack development, API design, authentication systems, and AI feature integration.

---


## 📌 Overview

The platform allows users to explore live cricket matches, analyze player performance, interact with an AI assistant, and gain predictive insights. It is designed with a clean UI and efficient backend architecture to simulate real-world production systems.

---

## ✨ Key Features

* Live match tracking with real-time score updates
* Detailed player analytics and historical performance
* AI-powered cricket assistant for intelligent Q&A
* Insights and predictions based on match data
* Secure authentication system (login/register)
* REST API-based scalable backend

---

## 🏗️ Tech Stack

Frontend: React.js, HTML, CSS, JavaScript
Backend: FastAPI (Python)
API: RESTful services
Database: SQLite or PostgreSQL
Tools: Git, GitHub, VS Code
Deployment: Vercel (frontend) and Render (backend)

---

## 📂 Project Structure

Cricket_stats/
│── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env

│── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json

│── README.md

---

## ⚙️ Installation & Setup

Clone the repository:

git clone [https://github.com/puneetbohra30-GREAT/Cricket_stats.git](https://github.com/puneetbohra30-GREAT/Cricket_stats.git)
cd Cricket_stats

Backend setup:

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend will run on: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Frontend setup:

cd frontend
npm install
npm start

Frontend will run on: [http://localhost:3000](http://localhost:3000)

---

## 🔐 Environment Variables

Create a .env file inside the backend folder and add:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60

---

## 📊 API Documentation

Base URL:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Authentication Endpoints:
POST /register → Register a new user
POST /login → Authenticate user

Cricket Data Endpoints:
GET /live → Fetch live match data
GET /players → Get player statistics
GET /schedule → View match schedule

AI Endpoints:
POST /chat → AI assistant responses
GET /insights → Match predictions and insights

---

## 🧠 Architecture

The React frontend communicates with the FastAPI backend through REST APIs. The backend handles business logic, authentication, and data processing. AI-related features generate intelligent responses and predictions, while the database manages user and cricket data efficiently.

---

## 🚀 Deployment

The application is designed for modern deployment:

* Frontend deployed on Vercel
* Backend deployed on Render
* Environment variables used for secure configuration

---

## 🎯 Future Enhancements

* Advanced analytics dashboard
* Real-time updates using WebSockets
* Machine learning-based prediction models
* Role-based authentication
* Improved mobile responsiveness

---

## 🤝 Contributing

Contributions are welcome. You can fork the repository, create a feature branch, commit your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Puneet Bohra
GitHub: [https://github.com/puneetbohra30-GREAT](https://github.com/puneetbohra30-GREAT)

---

⭐ Star this repository if you found it useful!
