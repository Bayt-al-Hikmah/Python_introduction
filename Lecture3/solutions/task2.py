n = int(input("Enter the number n :"))
for i in range(0,n+1):
    if i == 0 or i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
        elif j == i-1:
            print(i)
