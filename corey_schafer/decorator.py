def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print("in display function ")


decorated_display = decorator_function(display)

decorated_display()


#using Annotation

def decorator_function1(original_function):
    def wrapper_function1(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function1


@decorator_function1
def display1():
    print("in display function ")
#@decorator_function1 == display = decorator_function(display)
display1()


@decorator_function1
def display_info(name, age):

    print("display_info ran with arguments {} {}".format(name , age))


display_info("Pratik", 25)

