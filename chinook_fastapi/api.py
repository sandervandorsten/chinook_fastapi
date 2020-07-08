"""Main module."""

import json
import os
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dotenv import load_dotenv

app = FastAPI()

load_dotenv()


def read_data():
    with open(os.getenv("DATA_PATH")) as file:
        return json.load(file)


def write_data(data):
    with open(os.getenv("DATA_PATH"), "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)


class User(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    gender: Optional[str]
    ip_address: Optional[str]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users/")
def get_users():
    """Returns all users in the dataset"""
    users = read_data()
    return users


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    """Returns all users in the dataset"""
    users = read_data()

    if user_id not in [int(_id) for _id in users["users"]]:
        raise HTTPException(
            status_code=404, detail=f"User with user_id '{user_id}' not found"
        )
    else:
        return users["users"][str(user_id)]


@app.patch("/users/{user_id}", response_model=User)
async def update_user(user: User, user_id: int):
    """Allows (partial) updating information for a user.

    Args:
        user (User): Information for the user you want to update.
        user_id (int): user id from the user you want to update.

    Returns:
        [dict]: New values for the updated user
    """
    users = read_data()

    stored_user_data = users["users"][str(user_id)]
    stored_user_model = User(**stored_user_data)
    update_data = user.dict(exclude_unset=True)
    updated_user = stored_user_model.copy(update=update_data)
    users["users"][str(user_id)] = jsonable_encoder(updated_user)

    write_data(users)

    return updated_user
