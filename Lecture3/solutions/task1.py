a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

if a == 0 and b == 0:
    print("No equation")
elif a == 0:
    print("The solution is ",-c/b)
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        print("There is 2 solutions")
        x1 =(-b - delta ** (1/2)) / (2 * a)
        x2 =(-b + delta ** (1/2)) / (2 * a)
        print("x1 : ",x1)
        print("x2 : ",x2)
    elif delta == 0:
        print("There is only 1 solution")
        x = -b / (2 * a)
        print("x : ",x)
    else:
        print("There is no solution")