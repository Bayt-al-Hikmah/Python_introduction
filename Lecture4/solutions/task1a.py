def accept_solution(a:int ,b:int ,c:int)->bool:
    '''
    Function that check if ax^2+bx+c=0 accept solution
    it take a ,b ,c as argument and return the True or False 
    '''
    if a == 0 and b == 0:
        return False
    elif a ==0:
        return True
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return False
    return True
def solver(a:int ,b:int ,c:int,checker:bool)->float | str :
    '''
    Function that solve ax^2+bx+c=0
    it take a ,b ,c as argument and return the solution
    '''
    if checker(a,b,c):
        if a == 0:
            return -c / b
        delta = b ** 2 - 4 * a * c
        if delta == 0:
            return -b / (2 * a)
        else:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2))  / (2 * a)
            return x1, x2
    else:
        return "No solution"
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
print(solver(a,b,c,accept_solution))