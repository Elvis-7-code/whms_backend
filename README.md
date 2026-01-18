# Wahome Herd Management System (WHMS) — Backend

## Overview
This is the backend foundation for the Wahome Herd Management System (WHMS), a livestock farm management system designed to track animals individually, manage breeding, monitor feed usage, and send alerts.

This Day 8 build includes:
- Flask backend setup
- Database connection (PostgreSQL / SQLite)
- Core database models (Users, Animals, Breeding, Feed, Vaccinations, Alerts)
- Database migrations
- GitHub version control setup

---

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL (production) / SQLite (development)
- Git & GitHub

---

## Project Structure
```
whms-backend/
├── app/
│ ├── init.py #Where Flask app is created
│ ├── config.py #Config settings(DB URL, secret keys)
│ ├── extensions.py #Place for intializing SQLAlchemy, Migrate, JWT
│ ├── models/ #Databse tables
│ │ ├── user.py
│ │ ├── animal.py
│ │ ├── breeding.py
│ │ ├── feed.py
│ │ ├── vaccination.py
│ │ └── alert.py
│ └── routes/ #Routes(APIs)
│ └── auth_routes.py
├── run.py #Entry point to run the app
├── requirements.txt #Python packages needed
├── .env #Secret environment variablees
└── .gitignore #Files to ignore in Github(Like venv)
```

yaml
Copy code

---

## Database Models
- **Users:** id, name, email, password_hash, role (owner/manager/worker), created_at  
- **Animals:** id, tag_number, species, breed, sex, date_bought, is_pregnant, created_at  
- **Breeding:** id, bull_id, cow_id, start_date, end_date, expected_birth, status  
- **Feed Inventory:** id, feed_type, quantity_kg, daily_usage_kg  
- **Vaccinations:** id, animal_id, vaccine_name, scheduled_date, administered  
- **Alerts:** id, type (feed/pregnancy/vaccination), message, trigger_date, sent  

---

## Installation / Setup
```bash
# Clone the repository
git clone git@github.com:Elvis-7-code/whms_backend.git
cd whms_backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
(-Keeps dependencies seperate)
(-Ensures the project works exactly the same on any computer)

# Install dependencies
pip install -r requirements.txt

# Set environment variables (Linux / Mac)
export DATABASE_URL=your_database_url
export JWT_SECRET_KEY=your_secret_key

# Initialize and migrate database
flask db init #
flask db migrate -m "Initial tables"
flask db upgrade

# Run the backend
python run.py
Windows users: Use set DATABASE_URL=your_database_url and set JWT_SECRET_KEY=your_secret_key for environment variables.

## Day 9 – Authentication & Access Control

This day focused on securing the backend using JWT authentication and role-based access control.

### Features Implemented
- User registration with hashed passwords
- User login with JWT token generation
- Secure password storage using Werkzeug
- Protected API routes using JWT
- Role-based access control (Owner, Manager, Worker)

### Authentication Flow
1. User registers with name, email, password, and role
2. Password is hashed before storage
3. User logs in using email and password
4. System generates a JWT access token
5. Token is required to access protected routes

### Roles Supported
- Owner: Full system access
- Manager: Operational access
- Worker: Limited / read-only access

### Sample Endpoints
- POST `/api/auth/register`
- POST `/api/auth/login`
- GET `/api/auth/me` (JWT protected)

This authentication layer ensures the system is secure and ready for real farm usage before adding animal and breeding operations.
