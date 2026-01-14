# Basic Flask Notes App

A simple notes application built with **Flask** and **Flask-Login**, demonstrating user authentication and CRUD operations.  
This project exists in two variants to explore different types of databases:

- **SQLite version** – relational database approach
- **MongoDB (PyMongo) version** – document-based NoSQL approach

The goal of this project was to understand backend fundamentals, authentication flow, and the practical differences between SQL and NoSQL in a real Flask app.

---

## Features

- User authentication (signup, login, logout)
- Session management using Flask-Login
- Create and delete personal notes
- Notes scoped per user
- Server-side rendering using Jinja2
- Clean separation using data models instead of raw dictionaries

---

## Tech Stack

- **Backend:** Flask
- **Authentication:** Flask-Login
- **Databases:**
  - SQLite (SQLAlchemy-based version)
  - MongoDB (PyMongo-based version)
- **Templating:** Jinja2
- **Language:** Python 3

---

## Branches

- `main-sql`  
  Uses SQLite as the database. Follows a relational data model with tables and foreign-key style relationships.

- `main-pymongo`  
  Uses MongoDB with PyMongo. Implements document-based storage and manual relationships.

Both branches implement the same functionality to make comparison easier.

---

## Setup Instructions

### 1. Install uv (Modern Package Manager)
#### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
#### Windows (PowerShell)
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Restart your shell after installation.

### 2. Clone the repository
```bash
git clone https://github.com/qonstellations/Basic-Flask-Notes-App.git
cd Basic-Flask-Notes-App
```
### 3. Select a branch
```bash
git checkout main-sql
# or
git checkout main-pymongo
```
### 4. Sync dependencies and create a Virtual Environment using uv lock file
```bash
uv sync
```
### 5. Run the application
```bash
uv run main.py
```

### The app will be available at http://127.0.0.1:5000.

