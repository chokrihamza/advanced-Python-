def metadecortor(arg):
  def decorator_listedadd(addfun):
    def wrapper(args):
        return [addfun(val[0],val[1])**power for val in args]
    return wrapper
  if callable(arg):
     power=2
     return decorator_listedadd(arg)
  else:
     power=arg
     return decorator_listedadd


@metadecortor
def add(a,b):
    return a+b

print(add([(1,2),(2,3),(5,2),(4,5),(8,7),(9,10),(10,10),(20,20)]))