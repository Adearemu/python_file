
number = 10

def plusOne():
    global number
    number = 5
    return number + 1

def minusOne():
    return number - 1

def multiplyTwo():
    global number
    number = 15
    return number * 2

print(plusOne())
print(minusOne())
print(multiplyTwo())


# parameters and variables in a function are set to exist in the function's local scope
# parameters and variables outside of all functions are set to exist in the global scope


# Rules of Scope

# 1. Code in the global scope cannot use any local variable
# 2. Code in a local scope can access global variables
# 3. Code in one function's local scope cannot use variables in another function's local scope
# 4. Code in one function's local scope cannot use variables in any other local scope