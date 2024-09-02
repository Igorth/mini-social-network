# Social Network

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)](https://fastapi.tiangolo.com/)
[![Test Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-brightgreen)](https://pytest.org/)
[![CI/CD](https://github.com/Igorth/Mini-Social-Network/actions/workflows/python-app.yml/badge.svg)](https://github.com/Igorth/mini-social-network/actions)

## Overview

Mini Social Network is a Python project that simulates basic functionalities of a social networking platform. Users can register, create posts, send friend requests, and exchange messages. The project also includes a simple API layer built with FastAPI to handle user registration.

## Features

- **User Management**: Register users, login, and manage friends.
- **Posts**: Users can create, view, and delete posts.
- **Messaging**: Send and receive messages between users.
- **Friend Requests**: Send, accept, or reject friend requests.
- **API Integration**: Basic user registration API using FastAPI.
- **Testing**: Unit tests with `pytest`.

## Project Structure

```plaintext
├── src/
│   ├── main.py              # Main entry point for the application
│   ├── user.py              # User and UserManager classes
│   ├── post.py              # Post class
│   └── api.py               # FastAPI app for user registration
├── tests/
│   ├── test_user.py         # Unit tests for user functionalities
│   └── test_messaging.py    # Unit tests for messaging functionalities
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Files and directories to ignore in Git
```

## Installation
1. **Clone the repository:**
```commandline
git clone https://github.com/Igorth/Mini-Social-Network.git
cd Mini-Social-Network
```

2. **Create a virtual environment and activate it:**
```commandline
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the dependencies:**
```commandline
pip install -r requirements.txt
```
4. **Run the application:**
````commandline
python src/main.py
````

5. **Run the FastAPI server:**
````commandline
uvicorn src.api:app --reload
````

6. **Run the tests:**
```commandline
pytest tests/
```

## Usage
After setting up the project, you can start the application by running main.py to simulate user interactions 
like registering users, creating posts, and sending messages.

The FastAPI server can be started using uvicorn to test API endpoints for user registration.