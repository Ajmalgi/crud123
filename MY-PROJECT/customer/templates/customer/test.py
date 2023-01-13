def divide_dec(func):
    def wrapper(a,b):
        if b>a:
            a,b = b,a
        return func(a,b)
    return wrapper
@divide_dec
def divide(a,b):
    result = a/b
    print(result)

divide(2,10)