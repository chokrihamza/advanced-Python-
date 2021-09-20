""" declare our global decorator """
def meta_decorator(meta_args):
    meta_args()
    def decorator(fun):
        def wrapper(args):
            args()
            fun()

        return wrapper
    return decorator

def myfun():
    print("am out side of all these code")

@meta_decorator(myfun)
def fun_to_decorate():
    print("hello")

fun_to_decorate(myfun)