from dataclasses import dataclass

@dataclass
class User:
    user_id: str
    email: str
    name: str
    password: str
    image_url: str