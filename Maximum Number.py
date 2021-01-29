a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))
if a > b:
    d = a
    print(d)
else:
    d = b
if d > c:
    print("The maximum value: %s" %d)
else:
    print("The maximum value: %s" %c)