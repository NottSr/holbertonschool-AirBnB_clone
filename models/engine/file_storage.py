#!/usr/bin/python3
"""
Entry File Storage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes object/instances to a JSON file
    and deserializes JSON file to objects/instances
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """Return dictionary of <class>.<id> : object instance"""
        return self.__objects

    def new(self, obj):
        """
        function that sets in __objects the obj with key <obj class name>.id
        """
        """Add new obj to existing dictionary of instances"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        function that serializes __objects to the JSON file
        (path: __file_path); new_dict is a new dictionary in which
        the objects/instances have been replaced by their respective
        dictionary representation using the to_dict method from BaseModel
        """
        my_dict = {}

        for key, obj in self.__objects.items():
            """if type(obj) is dict:
            my_dict[key] = obj
            else:"""
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        function that deserializes the JSON file to __objects
        """
        """If json file exists, convert obj dicts back to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
