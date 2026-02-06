#!/usr/bin/python3
"""Module for serializing and deserializing custom Python objects."""
import pickle


class CustomObject:
    """A custom object representing a person's basic information.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.
    """
    def __init__(self, name, age, is_student):
        """Initializes the CustomObject with provided details.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in a formatted manner."""
        print("Name: {}\nAge: {}\nIs Student: {}".format(self.name,
                                                         self.age,
                                                         self.is_student))

    def serialize(self, filename):
        """Serializes the current object instance to a binary file.

        Args:
            filename (str): The path to the the object will be saved.
        """
        with open(filename, mode='wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserializes a binary file back into a CustomObject instance.

        Args:
            filename (str): The path to the file to be deserialized.

        Returns:
            CustomObject: The loaded object instance, or None if the file is
                missing, malformed, or corrupted.
        """
        try:
            with open(filename, mode='rb') as file:
                obj: cls = pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        return obj
