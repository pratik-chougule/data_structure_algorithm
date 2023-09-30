class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.'+ '@gmail.com'

    def full_name(self):

        return '{} {}'.format(self.first, self.last)


emp1 = Employee('pratik', 'Chougule')

print(emp1.first)
print(emp1.last)
print(emp1.full_name())