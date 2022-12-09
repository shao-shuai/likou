# Chekc if a string can be turned into a palindrome
from collections import Counter
def check(s):
    d = Counter(s)
    oddCount = 0

    for i in d.keys():
        if d[i] % 2 == 1: # you can use (d[i] & 1) == 1: as well
            oddCount += 1
            if oddCount > 1:
                return False


    return True

print(check("abbdfd"))
print(check("racecar"))
