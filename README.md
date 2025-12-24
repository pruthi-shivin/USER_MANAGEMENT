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

<ins> Virtual Environment(WINDOWS):	</ins>

python -m venv venv                         
venv\Scripts\activate

<ins> Virtual Environment(MAC):	</ins>

python3 -m venv venv 

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app
