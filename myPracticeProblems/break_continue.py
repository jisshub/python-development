# break

def breaKTheList(var):
    for each in var:
        if each == 5:
            break
        else:
            print(each)


var = [3, 4, 6, 5, 6, 7]

breaKTheList(var)


# continue
def continueTheList(var1):
    for eachItem in var1:
        if eachItem % 2 == 0:
            continue
        else:
            print(eachItem)


continueTheList(var1=[3, 4, 5, 6, 7])