def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(3,4,5)
multiply(3,4,5,6)