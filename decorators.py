def small(text):
    return text.upper()

print(small("Pratik"))

upper = small
print(upper("nikita"))



def shout(text):

    return text.upper()

def whisper(text):

    return text.lower()

def greet(func):

    # storing the function in a variable

    greeting = func("Hi, I am created by funcion passed as an argument")

    print(greeting)
greet(shout)
greet(whisper)







def addition(a,b):
    x = a/b
    print(x)
    return x

def smart_addition(func):

    def inner(a,b):
        if a < b:
            a,b = b,a

            return func(a, b)
    return inner

addition = smart_addition(addition)

addition(2,4)