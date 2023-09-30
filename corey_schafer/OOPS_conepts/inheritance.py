# in python inheritance is nothing but creating new sub class

class Employee:
    raise_amt = 1.04
    def __init__(self, name, email, salary):
        self.name= name
        self.email = email
        self.salary = salary

    def full_name(self):
        print(self.name +""+ self.email)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

#
# emp1 = Employee("Pratik", "pratik.gmail.com", 52000)
# emp2 = Employee("Nikita", "Nikita.gmail.com", 52000)
# print(emp1.name)
# print(emp2.name)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, name, email, salary, prog_laguage):
        # to inherite the __init__ method of super class
        super().__init__(name, email, salary)
        self.prog_language = prog_laguage

        # 2nd way of inherite the parent class
       # Employee.__init__(self, name, email, salary)

class manager(Employee):

    def __init__(self, name, email, salary, employees=None):
        super().__init__(name, email, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())





emp1 = Developer("Pratik", "pratik.gmail.com", 52000, 'Java')
emp2 = Developer("Nikita", "Nikita.gmail.com", 52000, 'Python')
print(emp1.email)
print(emp2.prog_language)

# print(emp1.salary)
# emp1.apply_raise()
# print(emp1.salary)
# #print(help(Developer))

mgr_1 = manager("Karan", "karan.com", 5500000, [emp1])
mgr_1.add_emp(emp1)
mgr_1.add_emp(emp2)
mgr_1.remove_emp(emp1)

mgr_1.print_emp()
#print(mgr_1.email)
#print(mgr_1.full_name())

print(isinstance(mgr_1, Developer)) # False bcos its not a instance of a current class

print(issubclass(Developer, manager))


