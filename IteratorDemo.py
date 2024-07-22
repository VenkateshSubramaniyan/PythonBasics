class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


def iterateFruits():
    it = iter(["Apple", "Mango", "Orange", "Banana"])
    print(next(it))
    while True:
        try:
            no = next(it)
            print(no)
        except StopIteration:
            break


iterateFruits()
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
