# 🚀 FastAPI User Authentication API with MySQL

This project is a simple and secure **User Authentication REST API** built using **FastAPI**, **SQLAlchemy**, **MySQL**, and **bcrypt** for password hashing.

---

## 🧩 Features

✅ User Registration  
✅ User Login with password verification  
✅ Password hashing using bcrypt  
✅ Data stored in MySQL database  
✅ Fully documented Swagger UI  
✅ Modular structure with SQLAlchemy models and Pydantic schemas

---


---

## ⚙️ Requirements & Dependencies

Install Python dependencies:

pip install -r requirements.txt


🛠️ Setup Instructions

1. Clone the Repository
git clone https://github.com/your-username/fastapi_user_app.git
cd fastapi_user_app

2. Create and Activate Virtual Environment (optional but recommended)
        # Create virtual environment
        python -m venv venv

        # Activate on Windows
        venv\Scripts\activate

        # Activate on macOS/Linux
        source venv/bin/activate
        
3. Install Dependencies
pip install -r requirements.txt

4. Configure MySQL Database
Make sure MySQL is running. Create a new database:

CREATE DATABASE fastapi_db;

Update DATABASE_URL in database.py:

DATABASE_URL = "mysql+mysqlconnector://<username>:<password>@localhost:3306/fastapi_db"
Replace <username> and <password> with your actual MySQL credentials.

5. Run the Application

uvicorn main:app --reload


🌐 API Endpoints
➕ POST /register
Registers a new user (with hashed password).

Request:
{
  "name": "Yasiru",
  "email": "yasiru@example.com",
  "password": "yourpassword"
}

🔑 POST /login
Logs in a user by verifying email and password.

Request:

{
  "email": "yasiru@example.com",
  "password": "yourpassword"
}


📑 API Docs
FastAPI auto-generates Swagger documentation:

http://127.0.0.1:8000/docs

📌 Next Steps (Optional)
🔐 Add JWT-based login and protected routes

📦 Add email verification and password reset

🛡️ Add role-based access control (admin/user)

📱 Connect with frontend (React/Flutter/etc.)

👨‍💻 Author
Yasiru Nadeesha – Software Engineer & Full-Stack Developer