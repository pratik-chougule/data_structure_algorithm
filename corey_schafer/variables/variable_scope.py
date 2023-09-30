'''
LEGB
L = "Local", E, ="Enclosing" G = "Global" B = "Built-in"


'''
#x = "global x"


def test(z):
    #global x
    #x = "local X"
    print(z)


test('local Z')
#print(x)

def my_min():
    pass
m = min([2,5,8,99,25])
print(m)

def outer():
    x = "outer X"

    def inner():
        nonlocal x
        x = "inner x"
        print(x)
    inner()
    print(x)
outer()