# flask-k8s-app
# ☸️ Flask + MongoDB + Kubernetes (Minikube Deployment)

This project demonstrates how to **build, containerize, and deploy** a Python **Flask web application** with a **MongoDB backend** using **Docker**, **Kubernetes**, and **Minikube**.  
It was designed as a practical exploration of **cloud-native microservice deployment**, following best practices in **container orchestration**, **scaling**, and **local cluster management**.

---

## 🧠 Project Overview

The main goal of this project is to show how a simple Flask web app can be deployed and scaled in a Kubernetes environment alongside a MongoDB database.  
It covers the entire process — from coding, containerizing, and configuring YAML manifests, to running the system inside a Minikube cluster.

---

## ⚙️ Architecture
             ┌──────────────────┐
             │   User / Client  │
             └───────┬──────────┘
                     │
                     ▼
             ┌──────────────────┐
             │ Flask Service     │
             │ (app-deployment)  │
             └───────┬──────────┘
                     │
                     ▼
             ┌──────────────────┐
             │ MongoDB Service   │
             │ (mongo-deployment)│
             └──────────────────┘


- **Flask App** → Handles API requests and interacts with MongoDB  
- **MongoDB** → Stores user data persistently  
- **Kubernetes** → Orchestrates containers and services  
- **Minikube** → Local cluster for testing and simulation of a cloud environment  

---

## 🧩 Key Features

- 🐳 **Dockerized Flask and MongoDB services**
- ☸️ **Deployed on Kubernetes (Minikube)**
- 🔁 **Service discovery via Kubernetes DNS**
- 📊 **Scalable and self-healing deployments**
- 🧾 **Declarative configurations using YAML manifests**
- 🧠 **Flask + PyMongo integration**
- 💻 **Local testing and browser-based access**

---

## 🧰 Technologies Used

| Layer | Technology |
|--------|-------------|
| **Backend Framework** | Python (Flask) |
| **Database** | MongoDB |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Package Manager** | pip |
| **Monitoring (optional)** | kubectl dashboard / logs |

---

## 🧱 Project Structure


