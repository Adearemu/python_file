# try catch and except

def div42By(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        return ("Error: You tried to divide by Zero")


print(div42By(2))
print(div42By(3))
print(div42By(0))
print(div42By(8))