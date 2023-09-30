class CSStudent:
    stream = "science"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


    def show_info(self):

        return 'i am {} and roll number is {}  studying {}'.format(self.name, self.roll_no, CSStudent.stream)

p1 = CSStudent('Pratik', 20)

print(p1.show_info())
