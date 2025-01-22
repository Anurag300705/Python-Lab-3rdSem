class cmp:
    a = 10
    b= 20

    def method1(args):
        print("Hello this is method1")  # Can also be used using self

    def method2(args,a,b):
        print(args.a + args.b)

    # def __init__(self):
    #     print("I am the constructor")  # This is default constructor

    def __init__(self,a,b):
        print(self.a + self.b) # Parametrized Constructor
    

obj1 = cmp()
# obj1 = cmp(30,50)  This is for parameterized constructor

# obj1.a = 20
obj1.address = "ABC 345"

print(obj1.a,end=' ')
print(obj1.b)
print(obj1.address)
# print(obj2.address)

obj1.method1()
# cmp.method1()
obj1.method2(obj1.a,obj1.b)

