class Person:
    a=20
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,var):
        self.__name=var
    @name.deleter
    def name(self):
        print(f'the value of {self.name} has been deleted ')
        del self.__name
person=Person('fdjgdf',20)
print(person.name)
print(person.name)
person.name="alex"
print(person.name)
del person.name

print(person.__dict__)