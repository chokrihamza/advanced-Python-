
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
# calss decorators
class add_decorator(object):
    def __init__(self,original_function):
     self.original_function=original_function

    def __call__(self,*args,**kwargs):
        print("the result of adding is:")
        return self.original_function(*args,**kwargs)
@add_decorator
def add(*a):
    print(sum(a))


#add_decorator(add)(1,2,3,4,5,6)

add(1,2,3,4,5) #