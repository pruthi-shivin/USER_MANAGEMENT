# USER_MANAGEMENT
A simple user management API built with FastAPI

-------------------------------

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic v2
- Pytest

-------------------------------

## Features

- Create a user
- Get user by ID
- Get users with pagination
- Update user details
- Test coverage with pytest

-------------------------------

## How to Run

git clone 
cd user-management-service

<u>Virtual Environment(WINDOWS):</u>
python -m venv venv                         
venv\Scripts\activate

<u>Virtual Environment(MAC):</u>
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app
