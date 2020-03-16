# get the minimum value in the array
def get_items_list(itemList):
    # check whether list is empty
    minValIndex = itemList.index(min(itemList))
    return minValIndex

#
# getIndex = get_items_list([4, 6, 10, 2, 5, 2])
# print(getIndex)
