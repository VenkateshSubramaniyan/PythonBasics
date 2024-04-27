def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    yield 4


# x is a generator object
x = simpleGeneratorFun()

print("Looping generator ")
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

print("Iterating generator ")
# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))

# Generator Expression
generator = (num ** 2 for num in range(10))
for num in generator:
    print(num)

# Fibonacci using Generator
def genFibanocciSeries():

    a=0
    b=1
    for x in range(1,10):
        yield a
        a,b = b, a+b
a= int(input("Enter number to print fibonacci").strip() or 10)
generator=genFibanocciSeries()
for i in range(1,a):
    print(next(generator))