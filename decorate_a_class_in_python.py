from datetime import datetime

class DateDecorator(object):
    # instance method decorator
    def instantMethodDecorator(self, func):
        def printDate(*args, **kwargs):
            print("Instance method decorator at time : \n", datetime.today())
            return func(*args, **kwargs)
        return printDate

    # class method decorator
    @classmethod
    def classMethodDecorator(self, func):
        def printDate(*args, **kwargs):
            print("Class method decorator at time : \n", datetime.today())
            return func(*args, **kwargs)
        return printDate


# decorator: instance method
a = DateDecorator()
@a.instantMethodDecorator
def add(a, b):
    return a+b

add(5,3)