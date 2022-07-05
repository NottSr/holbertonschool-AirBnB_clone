#!/usr/bin/python3
"""
Model BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """ Class BaseModel

    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ __init__ Method

        Public instance attributes:
            id: string - assigned with an uuid when an instance is created
            created_at: datetime - assigned with the current datetime when
                an instance is created.
            updated_at: datetime - assign with the current datetime when
                an instance is created and it will be updated every time
                you change your object.
        """
        
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ __str__ Class method

        Returns:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ save Class method

        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict Class method

        This method will be the first piece of the
        serialization/deserialization process.
        It was created a dictionary representation
        with “simple object type” of our BaseModel.

        A key __class__ was added to this dictionary with
        the class name of the object.
        Public instance attributes created_at and updated_at
        were converted to string object in ISO format.

        Returns:
            Dictionary containing all keys/values of
            __dict__ of the instance
        """

        c_dict = self.__dict__.copy()
        c_dict['__class__'] = self.__class__.__name__
        c_dict['created_at'] = self.created_at.isoformat()
        c_dict['updated_at'] = self.updated_at.isoformat()
        return c_dict
