class add_decorator:
    """ to work with class decorator we need the __call__ nethod"""
    def __init__(self,orignal_function,console="*"):
        self.orignal_function=orignal_function
        self.console=console

    def __call__(self,*args,**kwargs):
        print(self.console*20)
        self.orignal_function(*args,**kwargs)
        print(self.console*20)
@add_decorator
def add(*a):
    print(f'The result is: {sum(a)}')

add(12,20,20)