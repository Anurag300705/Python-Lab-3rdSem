def count_vowel(s):
    count = 0
    for i in s:
        if i in 'aeiou':
            count+=1
    return count+1

s = "Excellent and Superb"
print(f"The vowels in string s are {count_vowel(s)}")   