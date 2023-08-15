import os

from fastapi import FastAPI, HTTPException
import mysql.connector
from mysql.connector import errors

app = FastAPI()

try:
    db = mysql.connector.connect(
        host=os.environ.get('host'),
        user=os.environ.get('user'),
        password=os.environ.get('password'),
        database=os.environ.get('database')
    )
    cursor = db.cursor()
except errors.Error as err:
    print(f"Error connecting to MySQL: {err}")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/users")
def create_user(name: str, email: str):
    try:
        cursor.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        db.commit()
        user_id = cursor.lastrowid
        return {"user_id": user_id, "name": name, "email": email}
    except errors.Error as err:
        print(f"Error creating user: {err}")
        raise HTTPException(status_code=500, detail="Error creating user")

@app.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user[0], "name": user[1], "email": user[2]}
    except errors.Error as err:
        print(f"Error retrieving user: {err}")
        raise HTTPException(status_code=500, detail="Error retrieving user")
