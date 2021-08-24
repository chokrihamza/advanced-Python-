# example of agregation
from datetime import datetime
class Product:
    def __init__(self,name,quantity,price):
     self.name=name
     self.quantity=quantity
     self.price=price

class Order:

    order_number=0
    def __init__(self,name,product=[]):
        self.__number=Order.order_number
        self.__name=name
        self.__date=datetime.now()
        self.__products=product
        Order.order_number+=1
    def add_product(self,product):
        self.__products.append(product)
    @property
    def products(self):
        return [self.__products[i].__dict__ for i in range(len(self.__products))]
    def __price(self):
        prices=map(lambda product:product['price'],self.products)
        return (f'{sum(list(prices))}$')

    def invoice(self):
        print('*'*50)
        print(f'order N°\033[38;5;{180}m {self.__number} \033[0;0m')
        print('*' * 50)
        print(f'as a name\033[38;5;{150}m {self.__name} \033[0;0m')
        print('*' * 50)
        print(f'at \033[38;5;{200}m {self.__date} \033[0;0m')
        print('*' * 50)
        print(f'that contains \033[38;5;{250}m {self.products} \033[0;0m')
        print('*' * 50)
        print(f'Total Non TTC \033[38;5;{50}m {self.__price()} \033[0;0m')



product1=Product('cable',50,100)
product2=Product('switch',5,150)
product3=Product('router',3,100)
product4=Product('Rj45',70,50)
order1=Order('hardward devices',[product1,product2])
order1.add_product(product3)
order1.add_product(product4)
print(order1.order_number)
print(order1.products)
order1.invoice()



