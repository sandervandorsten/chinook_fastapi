#!/usr/bin/env python

"""Tests for `chinook_fastapi` package."""

from chinook_fastapi.api import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_read_root():
    """Testing init of API"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    users = response.json()
    assert "users" in users
    for user_id, user_data in users["users"].items():
        assert set(["first_name", "last_name", "email", "gender", "ip_address"]) == set(
            user_data.keys()
        )
