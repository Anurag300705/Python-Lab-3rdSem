def prime_factors(num):
  factors = []
  factor = 2
  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return factors

n = int(input("Enter a number: "))
print("The prime factors of",n,"are: ",prime_factors(n))