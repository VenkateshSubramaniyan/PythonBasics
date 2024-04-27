li=[
    ['John',2],
    ['Jim',9],
    ['Jason',1]
]
print(li)
li=sorted(li,key=lambda x: x[1])

print(li)

print ("**************")
intervals= [[1,4],[2,3]]
print(intervals)
intervals=sorted(intervals,key= lambda x:x[0])
print(intervals)
