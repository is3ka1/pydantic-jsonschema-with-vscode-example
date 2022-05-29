from pydantic import BaseModel

class User(BaseModel):
    """Represent a user, id is needed."""
    id: int
    name = "John Doe"
