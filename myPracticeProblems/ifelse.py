def newFunction(n):
    if n % 2 != 0:
        return "weird"
    elif n % 2 == 0 and n in [2, 3, 4, 5]:
        return "not weird"
    elif n % 2 == 0 and n in range(6, 21):
        return "weird"
    elif n % 2 == 0 and n > 20:
        return "not weird"


n = int(input("Enter Number: "))
print(newFunction(n))
