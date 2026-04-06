# Day 21: 30 Days of python programming

class Person:
    def __init__(self, first_name, last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def presentation(self):
        if len(self.last_name) == 0:
            return f"First name: {self.first_name}"
        return f"First name: {self.first_name}, Last name : {self.last_name}"


person = Person("Rayan", )

print(person.presentation())
