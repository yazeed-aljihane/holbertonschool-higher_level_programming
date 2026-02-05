#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Defines a student by first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in this
        list are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): A list of strings representing attribute
                names to fetch. Defaults to None.

        Returns:
            dict: A dictionary representation of the student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__

        new_dict = {}
        for item in attrs:
            if item in self.__dict__:
                new_dict[item] = self.__dict__[item]
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys are attribute names
                and values are the new values for those attributes.
        """
        for item in json:
            setattr(self, item, json[item])
