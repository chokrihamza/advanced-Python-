# in this part we are going to
# work with python using
# prefix decorators
def prefix_decorator(prefix):
  def add_decorator(func):
    def wrapper(*args,**kwargs):
        print(f'{prefix}','*'*20)
        func(*args,**kwargs)
        print(f'{prefix}','*' * 20)
    return wrapper
  return add_decorator




@prefix_decorator('Log')
def add(a,b):
    print(f'The sum is :{a+b}')


add(2,5)