import mod1

print(mod1.sample())
# gets the module name that is imported, since that module is executed from this
# python file - not directly by the python.

print(__name__)
# gives the __main__ as result since this file is executed by the python directly

