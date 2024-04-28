from pydantic import BaseModel, List
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum

class Gender(str,Enum):
    male= 'male'
    female = 'female'


class Role(str,Enum):
    admin = 'admin'
    user = 'user'

class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    mmiddle_name: str
    last_name: str
    gender: Gender
    roles = List[Role]