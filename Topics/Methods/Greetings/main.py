class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")

person_name = input()
person = Person(name=person_name)
person.greet()