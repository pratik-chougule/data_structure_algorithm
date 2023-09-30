from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person("Pratik", 28)

person2 = Person.from_birth_year("Sagar", 1996)

print(person1.age)
print(person2.age)
print(Person.is_adult(20))
