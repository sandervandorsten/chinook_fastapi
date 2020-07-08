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


def test_patch_user(user_id: int = 1):
    original_ip_address = client.get(f"/users/{str(user_id)}").json()["ip_address"]

    # Change the IP address of a user
    response = client.patch(f"/users/{str(user_id)}", json={"ip_address": "0.0.0.0"})
    assert response.status_code == 200
    assert response.json()["ip_address"] == "0.0.0.0"

    # Change it back to the original value
    response = client.patch(
        f"/users/{str(user_id)}", json={"ip_address": original_ip_address}
    )
    assert response.status_code == 200
    assert response.json()["ip_address"] == original_ip_address
