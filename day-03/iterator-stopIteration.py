"""
创建一个迭代器，最多迭代20次

raise StopIteration

"""
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myNumbers = MyNumber()

myiter = iter(myNumbers)

print(next(myiter))
print(next(myiter), "-----------", '---:::""""""')

for x in myiter:
    print(x, end=" ")