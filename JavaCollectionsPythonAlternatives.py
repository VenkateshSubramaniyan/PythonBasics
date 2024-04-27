# Below is list given in [], Python doesnt have array so no fixed size, list is used as array
a=[1,2,3,1]
print(type(a), a)

# Tuple in python
# Tuple is given in (). Tuple is similar to list but it is immutable
a=(1,2,3,1)
print(type(a), a)

# This is Set Given in {}
a={1,2,3,1}
print(type(a), a)

a={'a' :1,'b':2,'a':0}
print(type(a), a)


# Queue
from queue import Queue
names = Queue()
names.put("Alice")
names.put("Bob")
print(names.get())  # Output: Alice

# PRiority Queue

from collections import deque

names = deque()
names.appendleft("Alice")
names.append("Bob")

print(names.popleft())  # Output: Alice

# stack
# In Python, the built-in list data structure can be used as a stack by utilizing the append() and pop() methods.
names = []
names.append("Alice")
names.append("Bob")

print(names.pop())  # Output: Bob

# pip install sortedcontainers
#  Sorted set and Sorted Map
# In Python, the sortedcontainers module provides the SortedSet class
# from sortedcontainers import SortedSet
#     names = SortedSet(["Alice", "Bob", "Charlie"])
#     print(names)  # Output: SortedSet(['Alice', 'Bob', 'Charlie'])

# and SortedDict is provided by sortedcontainers[External]
# ages = SortedDict({"Alice": 30, "Bob": 25})
# print(ages)  # Output: SortedDict({'Alice': 30, 'Bob': 25})
