# cms-devops
# Complaint Management System

## About the Project

The **Complaint Management System** is a web-based application designed to make the process of registering, managing, and tracking complaints easier and more organized.

Users can register, log in, submit complaints, and track their complaint status. Administrators can view submitted complaints and update their status.

## Features

### User

* User registration
* User login and authentication
* Submit complaints
* View submitted complaints
* Track complaint status
* Secure logout

### Administrator

* Administrator login
* View complaint records
* View complaint details
* Update complaint status
* Manage submitted complaints

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Node.js, Express.js
* **Database:** SQLite
* **Authentication:** bcrypt and express-session
* **DevOps:** GitHub Actions

## Complaint Status

Complaints can be managed using different status values such as:

* Pending
* In Progress
* Resolved

## Project Structure

```text
Complaint-Management-System/
│
├── app.py
├── test_app.py
├── README.md
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

## CI/CD Pipeline

GitHub Actions is used to automate the testing process.

Whenever code is pushed to the `main` branch, the workflow:

1. Checks out the project code.
2. Sets up Python.
3. Installs required dependencies.
4. Runs automated tests.
5. Runs the Complaint Management System application.

```text
Developer
    ↓
Push Code
    ↓
GitHub Repository
    ↓
GitHub Actions
    ↓
Setup Environment
    ↓
Run Tests
    ↓
Test Passed
    ↓
Run Application
    ↓
Pipeline Successful
```

## Purpose

The project demonstrates how a digital complaint system can replace manual complaint handling and provide a more organized and transparent way to manage complaints.

## Project Version

**Version:** 1.0

## Team

**Complaint Management System — Full Stack Web Development Mini Project**
