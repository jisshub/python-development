# stack and queue operations using list
# numbers = []
# # stack
# numbers.append(30)
# numbers.append(16)
# numbers.append(15)
# numbers.append(13)
# print(numbers)
#
# # pop in list
# # numbers.pop()
# # print(numbers)
#
# # add an element
# numbers.append(77)
#
# print(numbers)
#
# # pop
# numbers.pop()
# print(numbers)

# stack and queue operation using deque

from _collections import deque

print(deque)
# deque is an object of collection class

# initialize a deque
numbers = deque()
numbers.append(55)
numbers.append(52)
numbers.append(54)
numbers.append(56)
numbers.append(57)
print(numbers)

# pop from deque
numbers.pop()
print(numbers)
numbers.append(90)
print(numbers)
print(numbers.popleft())
print(numbers.popleft())
print(numbers.popleft())

