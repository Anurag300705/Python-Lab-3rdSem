n = int(input("Enter the range for which you want sum: "))
sum = 0
pow = 0
for i in range(1,(n+1)):
    sum += i
    pow += i*i
print("The sum of", n ,"natural numbers is", sum)
print("The sum of squares of", n ,"natural numbers is", pow)  