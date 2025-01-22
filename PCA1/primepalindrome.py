def is_prime(num):
    if num < 2:
        return False
    count = 0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:        
        return True
    else:
        return False

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def generate_prime_numbers(n):
    primes = []
    num = 2  
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def find_palindrome_primes(n):
    primes = generate_prime_numbers(n)
    palindrome_primes = [p for p in primes if is_palindrome(p)]
    return palindrome_primes

# Example usage:
n = int(input("Enter the number of prime numbers to generate: "))
palindrome_prime_list = find_palindrome_primes(n)
print("Palindrome primes:", palindrome_prime_list)
