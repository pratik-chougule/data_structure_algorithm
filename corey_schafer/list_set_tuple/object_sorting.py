class employee():
    def __init__(self, name, age, salary):
        self.name= name
        self.age = age
        self.salary = salary
    def __repr__(self):

        return '({},{},{})'.format(self.name, self.age, self.salary)

from operator import attrgetter
e1 =employee("Pratik",28,12344)
e2 = employee("Nikita",23,22844)
e3 = employee("Sarita",45,84666)

emp_list =[e1,e2,e3]

def e_sort(emp):

    return emp.name

#s_employees = sorted(emp_list, key=e_sort)
s_employees = sorted(emp_list, key=lambda e: e.salary )
print(s_employees)
s_employees = sorted(emp_list, key=attrgetter('age') )

print(s_employees)
