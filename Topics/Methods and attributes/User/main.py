class User:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def user_information(self):
        print(f"{self.name} {self.surname} is {self.age} years old and lives in {self.country}.")

name = input()
surname = input()
age = int(input())
country = input()

user = User(name=name, surname=surname, age=age, country=country)
user.user_information()