class Person:

    # __init__ method is like default constructior in python
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overriden to string
    def __str__(self):
        return f"{self.name}({self.age})"

    # First parameter of any function is self object. Variable name is can be put any
    def myfunc(self):
        print("Hello my name is " + self.name)


if __name__ == '__main__':
    p1 = Person("John", 36)
    print(p1)
    p1.myfunc()
    # created object can be deleted like this
    del p1
    # print(p1) -> NameError: 'p1' is not defined
