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

2. docker compose up --build

3. test:
      curl -X POST http://localhost:8000/predict ^
      -H "Content-Type: application/json" ^
      -d "{\"home_elo\":1665,\"away_elo\":1588,\"home_squad_value\":340,\"away_squad_value\":210,\"home_form\":0.78,\"away_form\":0.44,\"home_goals_last5\":9,\"away_goals_last5\":4}"
