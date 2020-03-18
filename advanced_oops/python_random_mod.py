import random


# random.randint(a, b)
# generates a random integer b/w a and b, inclusive of both
def generate_numbers():
    rand_num = random.randint(10, 100)
    return rand_num


print(generate_numbers())


# random.choice()
def generate_numbers(get_names):
    # choice() -- accepts an iterable and returns
    # a random item from it
    rand_name = random.choice(get_names)
    return rand_name


names = ["jissmon", "jose", "akhil", "hari", "adharsh"]
print(generate_numbers(names))


# random.random() -- returns a random value b/w 0 and 1.
def get_random():
    try:
        value = random.random()
        return value
    except Exception:
        return Exception.args


print(get_random())


# random.shuffle() -- to shuffle a list of values
def shuffle_all():
    nums = list(range(10, 30))
    # shuffle values in the list
    random.shuffle(nums)
    print(nums)


shuffle_all()


# problems - 1
# shuffle()
def shuffle_2():
    get_nums = list(range(40, 100))
    random.shuffle(get_nums)
    return get_nums


print(shuffle_2())


# problem using randint()
def get_multipled():
    number = random.randint(30, 40)
    return number ** 3


print(get_multipled())
