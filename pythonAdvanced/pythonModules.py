print("import this module")

print("module imported")

def getprice(price):
    return f"Price is {price}"


# another function,
def getIndex(data, search_key):
    for key, value in data.items():
        if key == search_key:
            return value
    return -1


def enumerateFunc(fruits):
    for count, value in enumerate(fruits):
        print(count, value)




