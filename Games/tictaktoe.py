import random

def printGrid(grid):
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]} ")
    print("---|---|---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]} ")
    print("---|---|---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]} ")

def isSafe(grid):
    for i in range(3):
        if(grid[i][0]!="-" and grid[i][0]==grid[i][1] and grid[i][1]==grid[i][2]):
            return False
        if(grid[0][i]!="-" and grid[0][i]==grid[1][i] and grid[1][i]==grid[2][i]):
            return False
            
    if(grid[0][0]!="-" and grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]):
        return False
    if(grid[2][0]!="-" and grid[2][0]==grid[1][1] and grid[1][1]==grid[0][2]):
        return False
    
    return True

def tictaktoe(comp,player):
    gameGrid=[["-" for j in range(3)] for i in range(3)]
    turn=player
    while(True):
        if turn==player:
            print("Your turn")
            playerch=int(input("Choose between 1-9: "))
            if(not playerch in available):
                continue
        else:
            print("My turn")
            playerch=random.choice(available)
            print("My choice:",playerch)
        
        available.remove(playerch)
        row=(playerch-1)//3
        col=(playerch-1)%3
        
        if turn==player:
            gameGrid[row][col]=player
        else:
            gameGrid[row][col]=comp
            
        printGrid(gameGrid)
        if not isSafe(gameGrid):
            if turn==player:
                print("You won")
            else:
                print("I won")
            break
        elif(len(available)==0):
            print("It's a Tie")
            break
            
        if turn==player:
            turn=comp
        else:
            turn=player    
    
if __name__=="__main__":
    available=[1,2,3,4,5,6,7,8,9]
    players=["X","O"]
    while(True):
        player=input("Choose X or O: ")
        if player in players:
            players.remove(player)
            break
    comp=players[0]
    tictaktoe(comp,player)