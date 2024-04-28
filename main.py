'''
TO RUN => uvicorn main:app --reload

AYNCHIO, AWAIT AND ASYNC IN PYTHON: https://www.youtube.com/watch?v=K56nNuBEd0c

'''
from typing import List
from fastapi import FastAPI
from models import User,Gender, Role
from uuid import UUID,uuid4

app = FastAPI()

# temp database
db: List[User] = [
    User(id = uuid4(), first_name = "Azam",last_name="Afridi",gender=Gender.male, roles=[Role.student, Role.admin]),
    User(id = uuid4(), first_name = "Haroon",last_name="Khan",gender=Gender.male, roles=[Role.student])
]

@app.get('/')
async def root():
    return {"Hello":"World"}

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {'id':user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return ['deleted']
    return ['not found']