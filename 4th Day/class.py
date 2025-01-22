class base:
    a = 5

    def __init__(self):
        print("This is base constructor")

    def show(self):
        print(f"This is show in base class a = {self.a}")

class base1:

    def __init__(self):
        print("This is also the base class")

    def show1(self):
        print("This is show in base class")

class child(base):
    # def show(self):
    #     print("This is show in base class") Same class is not used as inheritance is used

    def extra(self):
        print("This is an extra method")

class child1(base,base1):
    # def show(self):
    #     print("This is show in base class")
    # super.__init__()
    def extra1(self):
        print("This is an extra1 method")

class child2(child1):
    a=5

a = base()
b = child()
c = child1()
d = child2()

# a.show()
# b.show()
# c.show()
# c.show1()
d.show()
d.show1()
d.extra1()