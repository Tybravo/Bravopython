import random
from turtledemo.penrose import start


class Employee:

    def __init__(self, name: str, age: int, role: str)-> None:
        self.__id = self.generate_id()
        self.__name = name.capitalize()
        self.__age = age
        self.__role = role


        def get_age(self):
            return self.__age


        def set_age(self, value):
            if value < 0:
                return ValueError("Invalid age")
            self.__age = value

    @staticmethod
    def generate_id():
            return "011"  + str(random.randrange(1,100))

    def __str__(self):
        return f"""
        id: {self.__id}
        Name: {self.__name}
        Age: {self.__age}
        Role: {self.__role}
        """


