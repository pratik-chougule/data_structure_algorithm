class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '.' + '@company.com'

    def full_name(self):

        return '{} {}'.format(self.first, self.last)
emp_1 = employee('Pratik', 'Chougule', 5000)
emp_2 = employee('Nikita', 'Chougule', 52999)

print(emp_1.first)
print(emp_2.first)
print('{}{}'.format(emp_1.first, emp_1.last))
print(emp_1.full_name())