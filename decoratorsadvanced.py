def decorator_listedadd(addfun):
    def wrapper(args):
        return [addfun(val[0],val[1]) for val in args]
    return wrapper




@decorator_listedadd
def add(a,b):
    return a+b

print(add([(1,2),(2,3),(5,2),(4,5),(8,7),(9,10),(10,10),(20,20)]))