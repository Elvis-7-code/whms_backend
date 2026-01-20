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

#Day 10- Animal managemenet & Protected Routes
 Day 10 focused on building core animal management functionality in the Wahome HErd management System (WHMS).
 The goal was to understand Flask routes, JWT protection and how backed APIs fetch data from the database securely.
 This day is very important because it introduces how real backend APIs work in production systems.

 ##Key Concepts Covered 
 1. Flask Blueprints
 2. Route decorators
 3. JWT-protected routes
 4. Returning JSON responses
 5. Understanding request --> logic --> response flow

 ###Features Implemented
 -Fetch all animals from the databasse 
 -Return structured  JSON data
 -Protect routes using JWT authentication

 @animal_bp.route(...)
 -This tells Flask which URL triggeres the function

 methods = ["GET"]
 -This route is for fetching data, not creating or updating.

 @jwt_required()
 -Only logged-in users with a valid JWT token can access this route.

 animals=Animal.query.all()
 -Fetches all animal records from the database.

 result = []
 -Creates an empty list to store formatted animal data.

 for animal in animals:
   result.append({
    "id": animal.id
    "tag_number":animal.tag_number,
    "species":animal.species,
    "breed": animal.breed,
    "sex": animal.sex,
    "is_pregnant":animal.is_pregnant
   });
 -Loops through each animal
 -Converts database object into JSON-frienfly dictionaries

 return jsonify(result), 200
 -Send the data back to the client with an HTTP 200 OK response

 ###Security
 - All animals routes are protected using Flask-JWT-Extended
 -Users must log in and attach a valid JWT token to access data

 ###Tools Used
 -Flask
 -Flask SQLAlchemy
 -Flask-JWT-Extended
 -Postman(for testing routes)

 ###Status
 -Animal routes implementes
 -JWT protection working
 -Data fetching tested successfully
 
 #Day 11 -- Breeding & Pregnancy Tracking
 **Overview**
 -Day 11 focused on designing the breeding logic for the Wahome Herd Management System (WHMS)

 The system now allows the farm to:
  -Track which male animals breed with females
  -Record start dates of breeding events
  -Predict expected birth dates using species-specific gestation preiods
  -Update female pregnancy status automatically
  -Prevent error like double-pregnancy or wrong species mating

  Breeding is treated as a seperate event in the system, not just a property of the female, allowing better historical tracking and future farm planning.

  ###Target Users
  -Farm Owner:can add males/females, start breeding and manually override records
  -Farm Manager:can view breeding records, start breeding, track pregnancies
  -Farm Worker: Can only view breeding and pregnancy statuses

  ###Animals Involved
  -Males: Bulls(cows),Rams(sheep), Goats
  -Females: Cows, Ewes, Goats
  -each animal has:
    .Unique tag number
    .Sex
    .Species
    .Pregnancy status(is_pregnant)

###Core Features Implemented
-Create breeding records linking male - female
-record start date of breeding 
-Calculate expected birth date based on gestation:
 .Cows- ~283days
 .Sheep- ~150days
 .Goats- ~150days
 -Update female's is_pregnant status automatically
 -Prevent breefing errors(double-pregnancy, wrong species)
 -Manual override allowed for special cases

 ###Breeding Workflow
 1.Male is added to the system
 2.Female exists in the system
 3.Breeding record is created linking male-female
 4.Start date of breeding is recorded
 5.Gestation period is applied
 6.Expected birth date is calculated automatically
 7.Female is marked as pregnant
 8.Alerts are scheduled for upcoming calving

 ###Error Handling/Validation
 -Male selected must match species
 -Female must exist
 -Female cannot be in the future
 -Start date cannot be in the future
 -Multiple births are supported and not treated as errors

 ###Route Endpoints(Planned for Coding)
 -POST/api/breeding/start -- Start breeding(Owner/Manager)
 -GET /api/breeding -- View all breeding records(Authenticated users)
 -GET /api/breeding/<id> -- View single breeding record
 These routes will handle logic like marking pregnancy, calculating expected births and validating breeding conditions.

 ###Outcome
 By the end of Day 11:
 -Breeding rules are clearly defined
 -Gestation periods are mapped
 -Error handling is identified
 -Workflow is fully documented
 -THe system is ready for actual coding of breeding functionality

 #Day 12 - Breeding Routes & Pregnancy Logic
 ##Overview
 DAy 12 focuses on coding the breeding functionality for WHMS.

 The system now allows the farm to:
 -Start a breeeding event linking a male (bull/ram) to a female (cow/ewe)
 -Automatically calculate the expected birth date based on species-specific gestation
 -Mark the female as pregnant in the animals table
 -Prevent invalid breeding events(species mismatch, double pregnancy)

 This forme the core of the farm's reproductive management and ensures accurate planning for fees, space, and care.

 __Target Users__
 ```
 Farm Owner: Can start breeding and override errors
 Farm Manager: Can start breeding and track pregnancy
 Farm Worker: can only view breeding records

```
***Core Features Implemented
-Start breeding: Create a new breeding record linking male- female
-Automatic pregnancy:Female is marked is_pregnant = True when breeding starts
-Expected birth calculations: Gestation period applied based on species:
   .Cow - 283days
   .Sheep - 150days
   .Goat - 150days

-Validation & error handling:
  .Male/female must exist
  .Species must match
  .Female cannot already be pregnant
-Manual override allowed for special cases

***Route Endpoints***
-POST /api/breeding/start - Start a breeding event(Owner/Manager)
  .Request body:{"male_id":1, "female_id":2}
  .Response: {"message": "Breeding started successfully", "female":"Tag123", "male":"Tag456", "expected_birth_date":"2026-06-18"}
-GET /api/breeding - View all breeding records(Authenticated users)
-GET /api/breeding/<id>-View a single breeding record

***Error Handling***
-Male must match species
-Female must exist
-Female cannot already be pregnant
-Start date cannot be in the future
-Multiple births are supported

***Outcome***
By the end of Day 12;
.Breeding routes are fully coded
.Pregnancy is automatically tracked
.Expected birth dates are calculated
.Systems validates breeding rules

## User Roles & Access Control

WHMS supports multiple users across different roles to reflect real-world farm operations. The system does not limit the number of owners, managers, or workers. Instead, access is controlled using role-based permissions.

### Supported Roles

- **Owner**
  - Full system access
  - Manage users (add/remove)
  - View all reports and alerts
  - Override system rules

- **Manager**
  - Manage daily farm operations
  - Record breeding activities
  - Update feed inventory
  - Manage vaccinations
  - View alerts

- **Worker**
  - View animal records
  - Update feeding records
  - Mark vaccinations as administered
  - Limited access (no administrative permissions)

### Authentication & Authorization

- Authentication is handled using JWT (JSON Web Tokens)
- Each JWT contains the user's role
- Access to routes is restricted based on role permissions

Example:
```python
@jwt_required()
def route():
    if current_user.role not in ['owner', 'manager']:
        return {"msg": "Unauthorized"}, 403

## Day 14 – System Automation & Alert Engine

Day 14 focuses on making WHMS intelligent, automated, and production-ready.

### Automation Features
- Automatic pregnancy prediction and tracking
- Daily feed depletion calculations
- Vaccination schedule generation
- Overdue task detection

### Alert Engine
- In-app alerts for critical farm events
- SMS alerts for owners and managers
- Alert types include:
  - Pregnancy alerts (14, 7, 3 days)
  - Feed low and critical alerts
  - Vaccination due alerts

### SMS Design
- SMS functionality is abstracted from routes
- Allows switching SMS providers without system changes

### Error Handling
- Authentication and authorization errors
- Data integrity validation
- System and integration failure handling

### Future Business Readiness
WHMS is designed to support future business features such as:
- Animal pricing
- Animal sales
- Market reporting

These features are planned in the data model but not implemented in the current phase.

### Maintenance Plan
- Daily system monitoring
- Weekly operational reviews
- Monthly vaccination audits
- Scheduled backups and optimization
