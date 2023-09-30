class Employee:
    #class variable
    raise_amount= 1.04
    def __init__(self, first, last, pay):
        #instance variables
        self.first = first
        self.last = last
        self.pay= pay
        self.eamil = first+'.'+last+"@ltimindtree.com"

    def full_name(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = self.pay * 4  #(using hard coded value)

        # using class variable
        # we can access the calss variables by using "self or class name
        self.pay = self.pay * self.raise_amount #Employee.raise_amount

emp1 = Employee("Pratik", "Chougule", 28)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
