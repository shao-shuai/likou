# 5 methods for solving palindrome problem

# Approach 1
def palindrome_1(str):
    return str == str[::-1]


# print(palindrome_1("Anne, I vote more cars race Rome-to-Vienna"))
# print(palindrome_1("llama mall"))
# print(palindrome_1("jmoney"))
# print(palindrome_1("abba"))

# Approach 2
# With for loop
# Note we only need to iterate to the middle
def palindrome_2(str):
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str) - 1 - i]:
            return False
    
    return True

# print(palindrome_2("abbabba")) 
# print(palindrome_2("abbaa"))
# print(palindrome_2("racecar"))

# Approach 3
# With while loop, 2 pointers

def palindrome_3(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        
        left += 1
        right -= 1

    return True

# print(palindrome_3("abbabba")) 
# print(palindrome_3("abbaa"))
# print(palindrome_3("racecar"))

# Approach 4
# With stack

def palindrome_4(str):
    stack = list(str)
    for i in str:
        x = stack.pop()
        if i != x:
            return False
    
    return True

# print(palindrome_4("abbabba")) 
# print(palindrome_4("abbaa"))
# print(palindrome_4("racecar"))

# Approach 5
# With recursion
def palindrome_5(str):
    if len(str) == 1:
        return True

    if str[0] != str[-1]:
        return False

    return palindrome_5(str[1:len(str) - 1])

print(palindrome_5("abbabba")) 
print(palindrome_5("abbaa"))
print(palindrome_5("racecar"))