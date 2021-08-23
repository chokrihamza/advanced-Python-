
def my_decorator(func):
    def wrapper():
        print("*"*50)
        func()
        print("*"*50)
    return wrapper

@my_decorator
def say_whee():
    print("Have a good day Python ")
    
#say_whee()

# this is a simple decorators in python

# decorators in python with arguments




def add_decorator(func):

    def wrapper(*args,**kwargs):
        print("the result of adding :")
        func(*args,**kwargs)
        print("end")
    return wrapper

@add_decorator
def add(*a):
    for val in a:
     print(val)

add(2,3)



