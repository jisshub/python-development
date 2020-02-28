# problem 2
# def superMarket(totalItems):
#     while totalItems > 0:
#         itemName = input("Item: ")
#         itemPrice = int(input("Price: "))
#         itemQuantity = int(input("Quantity Sold: "))
#         netPrice = itemQuantity * itemPrice
#         print(netPrice)
#         totalItems -= 1
#
#
# itemCount = int(input("Total Items: "))
# superMarket(itemCount)

# using OrderedDict()

from collections import OrderedDict


# create an ordered dict object


def myMarket(totalItems):
    Item_Dict = OrderedDict()

    while totalItems > 0:
        Item_Dict["item"] = input("Item Name: ")
        Item_Dict["price"] = int(input("Price :"))
        Item_Dict["quantity"] = int(input("Quantity Sold :"))
        net_Price = Item_Dict["price"] * Item_Dict["quantity"]
        totalItems -= 1
        print(Item_Dict["item"], Item_Dict["price"], net_Price)


itemCount = int(input("Total Items: "))
myMarket(itemCount)
