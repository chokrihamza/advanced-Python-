from datetime import datetime

class Add_DateDecorator(object):
    # instance method decorator
    def instantMethodDecorator(self, func):
        def printDate(*args):
            print('*'*40)
            print("Instance method decorator at time :", datetime.today())
            print('The result of sum is: ',func(*args))
            print('*' * 40)
        return printDate

    # class method decorator
    @classmethod
    def classMethodDecorator(self, func):
        def printDate(*args):
            print('*' * 40)
            print("Class method decorator at time : \n", datetime.today())
            print('The result of sum is: ',func(*args))
            print('*' * 40)
        return printDate


# decorator: instance method
a = Add_DateDecorator()
@a.instantMethodDecorator
def add(*a):
    return sum(a)

add(5,3)

# lets use the class method
@Add_DateDecorator.classMethodDecorator
def add(*a):
    return sum(a)

add(5,10)
