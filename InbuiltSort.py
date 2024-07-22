li = [
    ['John', 2],
    ['Jim', 9],
    ['Jason', 1]
]
print(li)
li = sorted(li, key=lambda x: x[1])

print(li)

print("**************")
intervals = [[1, 4], [2, 3]]
print(intervals)

intervals = sorted(intervals, key=lambda x: x[0])
print(intervals)

output = []
start, end = None, None
for interval in intervals:
    if start is None:
        start = interval[0]
        end = interval[1]
    elif interval[0] <= end:
        end = max(end, interval[1])
    elif interval[0] > end:
        output.append([start, max(end, interval[1])])
        start = interval[0]
        end = interval[1]

output.append([start, end])
print("ouput, ", output)
