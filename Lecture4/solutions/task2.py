from random import randint
goal = randint(1,30)
def take_value(msg: str)-> int:
    return int(input(msg))
def check_win(choice:int,goal:int) -> bool:
    if goal == choice:
        print("You guessed it right :D")
        return True
    elif choice >goal:
        print("Enter smaller Number")
    else:
        print("Enter bigger Number")
    return False


for i in range(5):
    choice = take_value("Try guess the number :")
    if check_win(choice,goal):
        print("it took you",i+1,"guesses")
        break
    elif i == 4:
        print("you lost the game :(")
print("the number was",goal)

