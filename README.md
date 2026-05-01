# ⚽ Football-ML-Compose

A containerized machine-learning application that predicts football match outcomes using team strength, form, and recent performance metrics.  
Built with **Python**, **FastAPI**, and **Docker Compose** for modular development, reproducibility, and easy deployment.

---

## 🧠 Overview

This project demonstrates how to orchestrate multiple services with Docker Compose:
- A **Trainer** service that preprocesses data, extracts features, and trains a classification model.
- An **API** service that loads the trained model and provides real-time predictions via a REST endpoint.
- A **Shared volume** that allows seamless communication between the two containers.

> Each component runs in its own container, yet they interact as a single cohesive system.

---

## 🏗️ Project Structure

football-ml-compose/
├─ docker-compose.yml
├─ README.md
├─ .env.example
├─ .dockerignore
├─ .gitignore
│
├─ trainer/
│ ├─ Dockerfile
│ ├─ requirements.txt
│ ├─ trainer.py
│ ├─ features.py
│ ├─ data/
│ │ └─ matches.csv
│ └─ model/
│ └─ (generated .pkl after training)
│
├─ api/
│ ├─ Dockerfile
│ ├─ requirements.txt
│ ├─ app.py
│ ├─ schema.py
│ └─ wait_for_model.py
│
└─ shared/


---

## ⚙️ Getting Started

### 1️⃣ Prerequisites
- **Docker Desktop** (Windows/macOS) or **Docker Engine + Compose** (Linux)
- Optional: `curl` or `Postman` for testing API endpoints

---

### 2️⃣ Setup & run

1. Clone the repository:
   ```bash
   git clone https://github.com/itu-itis24-kirteke21/Football-ML-compose.git
   cd Football-ML-compose
   ```

2. (Optional) Get a free API key from [football-data.org](https://www.football-data.org/) and set it in your environment:
   ```bash
   # On Windows (PowerShell)
   $env:FOOTBALL_API_KEY="your_api_key_here"
   # On Linux/macOS
   export FOOTBALL_API_KEY="your_api_key_here"
   ```

3. docker compose up --build

### 3️⃣ Accessing the Web UI

You can access the HTML web interface by opening your browser and navigating to:
`http://localhost:8000`

### 4️⃣ Testing the API

#### Predict a manual match:
```bash
curl -X POST http://localhost:8000/predict ^
-H "Content-Type: application/json" ^
-d "{\"home_elo\":1665,\"away_elo\":1588,\"home_squad_value\":340,\"away_squad_value\":210,\"home_form\":0.78,\"away_form\":0.44,\"home_goals_last5\":9,\"away_goals_last5\":4}"
```

#### Predict upcoming real matches:
Once you've set your `FOOTBALL_API_KEY`, you can fetch real upcoming Premier League fixtures and get predictions:
```bash
curl http://localhost:8000/predict-upcoming
```
