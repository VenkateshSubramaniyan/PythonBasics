'''
The Slice notation in python has the syntax -
    <object_name>[<start_index>, <stop_index>, <step>]
    given string/list/tuple, you can slice the said object using the format

ex: list
    list[<start>:<stop>:<step>]

'''

a = '1234'
a[::-1]
print (a)
print (a[::-1])
print (a[::2])
print (a[3:0:-1])