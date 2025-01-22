t1 = ("Hey", 1, 2)
t2 = (1, 4, 5, 7, 78)
t3 = (2, 3)

l = [t1, t2, t3]
longtup = max(l, key=len)


print("Longest tuple is: ", longtup)