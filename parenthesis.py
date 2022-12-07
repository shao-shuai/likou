def parenthesis(str):
    b = 0

    for i in str:
        if i == "(":
            b += 1
        elif i == ")":
            b -= 1
            if b < 0:
                return False
    
    return b == 0

print(parenthesis("(())()"))

# https://leetcode.com/problems/valid-parentheses/description/
# Leetcode 20 parenthesis