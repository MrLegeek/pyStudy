class Temp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print('func1')

    def func2(self):
        print(self.name)
        self.func1()

if __name__ == '__main__':

    obj1 = Temp('shaw', 25)
    obj1.func1()
    obj1.func2()
