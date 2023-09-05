
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper execute this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function
class decorator_class(object):

    # __init__ will tie our function with instance of this class
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executes this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def desplay():
    print("in display function")


desplay()