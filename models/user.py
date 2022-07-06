#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    Defines attributes/methods for the User class, subclass of BaseModel
    Other attributes/methods are inherited from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
