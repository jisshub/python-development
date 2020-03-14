# Exception
def func_one(var1):
    return var1, var5


def func_two(var3):
    return var3


def func_four(var4):
    return var4


try:
    # print(func_three(50))
    print(func_one(44))
except Exception:
    print(func_two(55))
finally:
    print(func_four(50))

# Exception in try block force it to terminate and that exception is caught by except block
# code in except block executes and later finally block
