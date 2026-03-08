class Test(Exception):
    pass

def func(num):
    if num < 0:
        raise Test("Negative number is not allowed")
    return num * 2  


func(-5)