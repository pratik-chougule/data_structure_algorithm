class A():
    def __init__(self):
        super().__init__()
        self.x = 1

# parent class B
class B():
    def __init__(self):
        super().__init__()
        self.y = 2

# parent class C
class C():
    def __init__(self):
        self.z = 3

# target class D
class D(A, B, C):
    def __init__(self):
        super().__init__()

d = D()
print(vars(d))


class Father:
    def __init__(self, fname):
        super().__init__()
        self.fname = fname

    def display_f(self):

        print(self.fname)

class Mother:

    def __init__(self, mname):
        self.mname = mname

    def displya_m(self):
        print(self.mname)


class child(Father, Mother):
    def __init__(self, fname, mname, cname):

        self.cname = cname

    def display_info(self):

        print("{dislpyainfo}", {self.cname}+" "+ {self.fname}+" "+{self.mname})



child_obj = child("Pratik", "Laxman", "Sarita")

print(child_obj.cname)


