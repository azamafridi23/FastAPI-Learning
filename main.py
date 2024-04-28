'''
TO RUN => uvicorn main:app --reload

AYNCHIO, AWAIT AND ASYNC IN PYTHON: https://www.youtube.com/watch?v=K56nNuBEd0c

'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    await foo()
    return {"Hello":"World"}