#!/bin/usr/python3

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User object

        ARGUMENTS:
        ----------
        email (string): user email
        password (string): user account password
        first_name (string): users' first name
        last_name (string): users' last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
