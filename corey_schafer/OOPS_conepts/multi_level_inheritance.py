class Grand_father:

    def __init__(self, grand_father_name):

        self.grand_father_name = grand_father_name


class Father(Grand_father):
    def __init__(self, father_name, grand_father_name):
        self.father_name = father_name
        
        Grand_father.__init__(self, grand_father_name)

class son(Father):
    def __init__(self, son_name, father_name, grand_father_name):

        self.son_name=son_name

        Father.__init__(self, father_name, grand_father_name)

    def print_names(self):
        print("Grandfather name :", self.grand_father_name)
        print("father name is :",self.father_name)
        print("son name is :", self.son_name)

son1 = son("Pratik", "Laxman", "Rau")

son1.print_names()