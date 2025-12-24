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

<ins>STEP-1: Clone the Repository</ins><br>
git clone https://github.com/pruthi-shivin/USER_MANAGEMENT <br>
cd user-management-service

<ins>STEP-2: Setup the Virtual Environment</ins><br>
<ins> Virtual Environment(WINDOWS):	</ins>

python -m venv venv                         
venv\Scripts\activate

<ins> Virtual Environment(MAC):	</ins>

python3 -m venv venv<br> 
source venv/bin/activate

<ins>STEP-3: Install the requirements</ins><br>
pip install -r requirements.txt

<ins>STEP-4: Run the app</ins><br>
uvicorn app.main:app
