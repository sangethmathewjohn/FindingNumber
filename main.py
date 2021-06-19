import random

ans = random.randint(1,100)
def check(cguess,guess):
    if guess>cguess:
        print("Too High")
        return True
    elif guess<cguess:
        print("Too Low")
        return True
    elif guess==cguess:
        print(f"Good you found the number {cguess} ")
        return False  


def level(difficulty):
    for i in range(difficulty):
        guess=int(input("Make your guess: "))
        while not check(ans,guess):
            exit()
        print(f"You have {difficulty-(i+1)} chance more!!!")
    print(f"You were not able to find the number {ans}!!!")
        
   
print("Welcome to the number Guesisng Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose difficulty level easy, medium or hard  :")
if difficulty=="easy":
    diffy =10
elif difficulty=="medium":
    diffy=7
else:
    diffy=5
level(diffy)   

            
    

           

