from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional


@dataclass
class User:
    id: str
    name: str
    email: str
    primary_mobile: str
    secondary_mobile: Optional[str]
    aadhaar: str
    pan: str
    date_of_birth: date
    place_of_birth: str
    current_address: str
    permanent_address: str
    created_at: datetime
