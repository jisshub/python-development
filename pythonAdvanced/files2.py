# here v import pythonModules file
import pythonModules as pm


# call the function using this module name
v = pm.getprice(60)
print(v)

# running another function
v = pm.getIndex({"a": "jissmon", "b": "jose", "c": "abin"}, "c")
print(v)

# new function
pm.enumerateFunc(["apple", "banana", "grapes"])

