import random

tuple=("stone","paper","scissor")

points=[0,0,10]
#comp,user,maxpoint

def compwin():
    points[0]+=1
    print("I got a point")
    
def userwin():
    points[1]+=1
    print("You got a point")
    
def game(comp,user):
    print("You:",user)
    print("Me:",comp)
    
    if comp==user:
        print("It was a tie")
    elif comp=="stone":
        if user=="paper":
            userwin()
        else:
            compwin()
    elif comp=="paper":
        if user=="stone":
            compwin()
        else:
            userwin()
    else:
        if user=="stone":
            userwin()
        else:
            compwin()
            
    print("Your points:",points[1])
    print("My points:",points[0])

def spsgame():
    print("Enter 0 for Stone")
    print("Enter 1 for Paper")
    print("Enter 2 for Scissor")
    
    while points[0]<points[2] and points[1]<points[2]:
        while True:
            compch=random.choice(tuple)
            print("")
            userin=int(input("Your Choice: "))
            if userin>=0 and userin<=2:
                break
            else:
                print("Choice Not Valid! Enter Again")

        userch=tuple[userin]
        game(compch,userch)

    print("")
    if points[0]==10:
        print("    I won the match!")
    else:
        print("    You won the match!")
    
while True:
    spsgame()
    print("")
    wantplay=input("Want to play again? (Yes/No):").lower()
    if wantplay=="no":
        break
    else:
        points=[0,0,10]