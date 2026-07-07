```markdown
# 🏏 Cricket Stats AI

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=28&duration=3000&color=00C2FF&center=true&vCenter=true&width=700&lines=Cricket+Analytics+Platform;Real-Time+Match+Insights;AI-Powered+Cricket+Assistant;FastAPI+%2B+React+Full+Stack+App" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/API-REST-orange?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/puneetbohra30-GREAT/Cricket_stats?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/puneetbohra30-GREAT/Cricket_stats?style=for-the-badge" />
</p>

---

## 📌 Overview

**Cricket Stats AI** is a full-stack web application designed to deliver **real-time cricket data, player analytics, and AI-powered insights**.  
It combines modern frontend technologies with a high-performance backend to create a scalable and intelligent sports analytics platform.

This project demonstrates:
- Full-stack development (React + FastAPI)
- API design & integration
- Authentication systems
- AI-driven features and insights

---

## 🚀 Live Demo

🌐 Frontend (Vercel):  
https://your-frontend-url.vercel.app  

⚙️ Backend API (Render):  
https://your-backend-url.onrender.com  

---

## ✨ Key Features

- 🔴 **Live Match Tracking** — Real-time cricket score updates  
- 📊 **Player Analytics** — Performance statistics and history  
- 🤖 **AI Assistant** — Ask cricket-related queries intelligently  
- ⚡ **Insights Engine** — Smart predictions and analysis  
- 🔐 **Authentication** — Secure login & registration system  
- 🌐 **REST API Integration** — Scalable backend architecture  

---

## 🏗️ Tech Stack

| Category        | Technology              |
|----------------|------------------------|
| Frontend       | React.js               |
| Backend        | FastAPI (Python)       |
| API            | RESTful Services       |
| Database       | SQLite / PostgreSQL    |
| Styling        | CSS / Modern UI Design |
| Deployment     | Vercel + Render        |
| Tools          | Git, GitHub, VS Code   |

---

## 📂 Project Structure

```

Cricket_stats/
│── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env
│
│── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
│
│── README.md

````

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/puneetbohra30-GREAT/Cricket_stats.git
cd Cricket_stats
````

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will run at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will run at:
👉 [http://localhost:3000](http://localhost:3000)

---

## 🔐 Environment Variables

Create a `.env` file inside `backend/`:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 📊 API Documentation

Base URL:

```
http://127.0.0.1:8000
```

### 🔑 Authentication

| Method | Endpoint  | Description       |
| ------ | --------- | ----------------- |
| POST   | /register | Register new user |
| POST   | /login    | User login        |

---

### 🏏 Cricket Data

| Method | Endpoint  | Description           |
| ------ | --------- | --------------------- |
| GET    | /live     | Get live match data   |
| GET    | /players  | Get player statistics |
| GET    | /schedule | Match schedule        |

---

### 🤖 AI Features

| Method | Endpoint  | Description                   |
| ------ | --------- | ----------------------------- |
| POST   | /chat     | AI cricket assistant response |
| GET    | /insights | Match predictions & insights  |

---

## 🧠 Architecture

* **Frontend (React)** communicates with backend via REST APIs
* **FastAPI backend** handles business logic and data processing
* **AI module** generates intelligent responses and predictions
* **Database layer** stores user and match-related data

---

## 🚀 Deployment

* **Frontend:** Vercel
* **Backend:** Render

Steps include:

* Build frontend → deploy on Vercel
* Deploy FastAPI backend → Render
* Connect via environment variables

---

## 🎯 Future Enhancements

* Advanced data visualization dashboards
* Real-time WebSocket updates
* Machine learning prediction models
* Role-based authentication system
* Mobile-first UI optimization

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Puneet Bohra**
GitHub: [https://github.com/puneetbohra30-GREAT](https://github.com/puneetbohra30-GREAT)

---

<p align="center">
  ⭐ Star this repository if you found it useful!
</p>
```
