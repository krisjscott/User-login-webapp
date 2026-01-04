# 🔐 User-login-webapp

## 📌 What this is

This is a simple Django-based web application that demonstrates how to build a **user login system** with a landing page for authenticated users. It uses Django’s built-in authentication and keeps the UI clean and minimal using templates.

<!-- 📷 Add a screenshot of your app here -->
<!-- ![Login Page](images/login.png) -->

---

## ⚙️ How to set it up locally

Follow these steps to run the project on your system.

### 🧩 Prerequisites

Make sure you have:
- Python (3.x recommended)
- `pip` installed

---

### 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/krisjscott/User-login-webapp.git
   ```

2. **Move into the project directory**
   ```bash
   cd User-login-webapp
   ```

3. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate         # Windows
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### 🗄️ Database setup

This project uses **SQLite** by default.

Run migrations to set up the database:
```bash
python manage.py migrate
```

---

### ▶️ Running the app

Start the Django development server:
```bash
python manage.py runserver
```

Open your browser and visit:
```
http://localhost:8000/
```

---

## 🧠 How it works

The application includes:
- 🔑 A **login page** for user authentication  
- 🏠 A **main page** accessible only after login  
- 🍪 Session handling using Django’s built-in auth system  

---

## 📂 What’s inside

This repository contains:
- Django project files (`manage.py`, settings, URLs)
- HTML templates for login and main pages
- SQLite database for local development

<!-- 📷 Add more UI screenshots here -->
<!-- ![Dashboard](images/dashboard.png) -->

---

## 🚀 Next steps

Ideas you can build on:
- 👤 User registration (signup)
- 🔁 Password reset & email verification
- 🎨 Better styling and responsive layout

---

## 📄 License

Add a license of your choice (MIT, GPL, etc.).

---

## 👨‍💻 Credits

Built by **Krish Kumar** using Django 🐍
