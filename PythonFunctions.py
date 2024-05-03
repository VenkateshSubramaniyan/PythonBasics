"""
1) Function Syntax
def function_name(parameter: data_type) -> return_type:
    # body of the function
    return expression
    """


def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3


num1, num2 = 5, 15
print(f"The addition of {num1} and {num2} results {add(num1, num2)}.")


# 2) Default argument
def myFun(x, y=50):
    print("x: ", x, " y:", y)
myFun(10)

# 3) Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)

# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

 # 4) Arbitrary Keyword  Arguments
# *args in Python (Non-Keyword Arguments)  -> like list of elements
# **kwargs in Python (Keyword Arguments) -> like map

# (Non-Keyword Arguments)
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# (Non-Keyword Arguments)
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')

# 5) Python Function within Functions
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()
f1()

#6) Annonymous Functions
def cube(x): return x*x*x   #Annonymous Function
cube_v2 = lambda x : x*x*x #Lambda Fnction

print(cube(7))
print(cube_v2(7))