class person:

    def __init__(self, name, company):
        self.name = name
        self.company = company

    # def show(self):
    #     print("i am " + self.name + " working in a " + self.company)


    def __repr__(self):

        return  f"my name is {self.name} and working in {self.company}"


p1 = person("Pratik", "Ltimindtree")
print(p1)
#p1.show()
