def is_prime(n: int) -> bool :
    '''
    This function take number as argument and check if it is prime
    '''
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True
def print_primes(n:int,checker:bool) -> int:
    '''
    This function take 2 argument number n and checker
    - n is number
    - checker is function that check if number is prime
    then it print all the number from 0 to n 
    '''
    for i in range(2,n+1):
        if checker(i):
            print(i)
number = int(input("Enter number :"))
print_primes(number,is_prime)