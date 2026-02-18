# 🏨 Hotel Management System (Django Based)

## 📌 Project Overview

This is a web-based Hotel Management System developed using Django framework.
The system helps manage hotel operations including room management, booking, customer records, billing, and administrative controls.

This project demonstrates backend development, database integration, authentication system, and CRUD operations using Django.

---

## 🚀 Features

* Admin Login System
* Room Management (Add / Update / Delete Rooms)
* Customer Registration
* Room Booking System
* Billing & Transaction Management
* Check-in / Check-out Handling
* Dashboard Overview
* Responsive UI

---

## 🛠 Technology Stack

* Python 3.x
* Django 3.x
* SQLite3 (Default Database)
* HTML5
* CSS3
* Bootstrap
* JavaScript

---

## 📂 Project Structure

Hotel_Management_System/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── templates/
├── static/
├── app/
└── README.md

---

## ⚙️ Installation & Setup Instructions

### 1️⃣ Clone or Extract Project

Extract the project folder or clone repository.

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install django
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

Enter username, email, and password.

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin
```

---

## 🔐 Default Database

* Uses SQLite3 (auto-created after migration)
* Can be switched to MySQL / PostgreSQL if needed

---

## 📊 System Modules

1. Authentication Module
2. Room Management Module
3. Booking Management Module
4. Billing System
5. Admin Control Panel

---

## 🎯 Purpose of Project

This project demonstrates:

* Django MVC architecture
* CRUD operations
* Database relationships
* Form handling
* Authentication & Authorization
* Full-stack integration

---

## 🧩 Future Improvements

* Online Payment Gateway Integration
* Email Notification System
* REST API Integration
* Multi-user Role Management
* Advanced Reporting Dashboard

---

## 👨‍💻 Developed For

Academic / Learning / Practice Purpose

---

## 📄 License

This project is developed for educational purposes only.
