class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


person1 = Person("Pratik", 12)

person1.display()


class employee(Person):

    def Print(self):
        print("employee class called")
emp_deatils = employee("Sagar", 22)
emp_deatils.display()

#calling child function
emp_deatils.Print()