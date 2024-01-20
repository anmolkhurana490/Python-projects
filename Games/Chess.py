import gc
class Box:
    def __init__(self,row,col):
        self.row=row
        self.col=col
    color="white"
    piece=None
    
class WhitePiece:
    def __init__(self,piecetype):
        self.piecetype=piecetype
    
    color="white"
    notMoved=True
    king=None
    
    whitePieces=[]
    deadWhite=[]
    
class BlackPiece:
    def __init__(self,piecetype):
        self.piecetype=piecetype
        
    color="black"
    notMoved=True
    king=None
    
    blackPieces=[]
    deadBlack=[]
        
dirlist=[(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,1),(-1,0),(-1,-1)]
    
def isKingSafe(turn):
    for row in board:
        for box in row:
            opponentPiece=box.piece
            if opponentPiece!=None and opponentPiece.color!=turn.color:
                if turn.king in showPossibleMoves(box):
                    return False
    return True                
        
def legal(piece,newrow,newcol):
    if board[newrow][newcol].piece!=None:
        if board[newrow][newcol].piece.color==piece.color:
            return False
    #if self.isKingSafe(newrow,newcol):
        return True
    else:
        return True
        
def kingMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in dirlist:
        newrow=row+i
        newcol=col+j
        if insideBoard(newrow,newcol):
            if legal(piece,newrow,newrow):
                moveList.append((newrow,newcol))
                    
    return moveList
        
def queenMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in dirlist:
        newrow=row
        newcol=col
        while True:
            newrow+=i
            newcol+=j
            if insideBoard(newrow,newcol):
                if legal(piece,newrow,newcol):
                    moveList.append((newrow,newcol))
                if board[newrow][newcol].piece!=None:
                    break
            else:
                break
                    
    return moveList            
        
def rookMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in dirlist:
        if i!=0 and j!=0:
            continue
        newrow=row
        newcol=col
        while True:
            newrow+=i
            newcol+=j
            if insideBoard(newrow,newcol):
                if legal(piece,newrow,newcol):
                    moveList.append((newrow,newcol))
                if board[newrow][newcol].piece!=None:
                    break
            else:
                break
                    
    return moveList            
                    
def bishopMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in dirlist:
        if i==0 or j==0:
            continue
        newrow=row
        newcol=col
        while True:
            newrow+=i
            newcol+=j
            if insideBoard(newrow,newcol):
                if legal(piece,newrow,newcol):
                    moveList.append((newrow,newcol))
                if board[newrow][newcol].piece!=None:
                    break
            else:
                break
                    
    return moveList            
                    
def knightMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]:
        newrow=row+i
        newcol=col+j
        if insideBoard(newrow,newcol):
            if legal(piece,newrow,newcol):
                moveList.append((newrow,newcol))
                
    return moveList        
    
def pawnMoves(row,col):
    moveList=[]
    piece=board[row][col].piece
    for i,j in [(2,0),(1,0),(1,-1),(1,1)]:
        if i==2 and not piece.notMoved:
            continue
        if piece.color=="white":
            newrow=row+i
            newcol=col+j
        else:
            newrow=row-i
            newcol=col-j
            
        if insideBoard(newrow,newcol):
            if j==0 and board[newrow][newcol].piece!=None:
                continue
            elif j!=0 and board[newrow][newcol].piece==None:
                continue
            if legal(piece,newrow,newcol):
                moveList.append((newrow,newcol))
                    
    return moveList
        
def promotion(piecetype):
    piece=newPiece(self.color,piecetype)
    if self.color=="white":
        whitePiece.remove(self)
        deadWhite.append(self)
    else:
        whitePiece.remove(self)
        deadWhite.append(self)
            
    return piece        
                    
letter=["a","b","c","d","e","f","g","h"]

def createBoard():
    board=[]
    for row in range(8):
        board.append([])
        for col in range(8):
            box=Box(row,col)
            if (row+col)%2 != 0:
                box.color="black"
            board[row].append(box)
    return board
    


moveDic={}


def insideBoard(i,j):
    if i>=0 and i<=7 and j>=0 and j<=7:
        return True
        
def newPiece(pieceColor,piecetype):
    
    if pieceColor=="white":
        piece=WhitePiece(piecetype)
        piece.whitePieces.append(piecetype)
    else:
        piece=BlackPiece(piecetype)
        piece.blackPieces.append(piecetype)
    return piece
    
def assignPieces(pieceColor,position):
    for i,piecetype in enumerate(["rook","knight","bishop","king","queen","bishop","knight","rook"]):
        piece=newPiece(pieceColor,piecetype)
        board[position][i].piece=piece
        
    for n in range(8):
        pawn=newPiece(pieceColor,"pawn")
        if position==0:
            board[1][n].piece=pawn
        else:
            board[6][n].piece=pawn
                

def showPossibleMoves(currentbox):
    piecetomove=currentbox.piece
    if piecetomove==None:
        return
    row=currentbox.row
    col=currentbox.col
    if piecetomove.piecetype=="king":
        possMoves=kingMoves(row,col)
    elif piecetomove.piecetype=="queen":
        possMoves=queenMoves(row,col)
    elif piecetomove.piecetype=="rook":
        possMoves=rookMoves(row,col)
    elif piecetomove.piecetype=="knight":
        possMoves=knightMoves(row,col)
    elif piecetomove.piecetype=="bishop":
        possMoves=bishopMoves(row,col)
    else:
        possMoves=pawnMoves(row,col)
        
    return possMoves
    
def movePiece(prebox,newbox,possMoves):
    piecetomove=prebox.piece
    if piecetomove==None:
        return
    newrow=newbox.row
    newcol=newbox.col
    if (newrow,newcol) in possMoves:
        info={
            "piece": (piecetomove.piecetype,prebox.piece.color),
            "prebox": f"{letter[prebox.col]}{prebox.row+1}",
            "newbox": f"{letter[newcol]}{newrow+1}",
            "cuts": None,
            "promoted": None
        }
        
        if piecetomove.piecetype=="king":
            if piecetomove.color=="white":
                WhitePiece.king=(newrow,newcol)
            else:
                BlackPiece.king=(newrow,newcol)
            
        prebox.piece=None
        if newbox.piece!=None:
            deadPiece(newbox.piece)
            info["cuts"]=(newbox.piece.piecetype,newbox.piece.color)
            
        newbox.piece=piecetomove
        if piecetomove.piecetype=="pawn" and (newrow==0 or newrow==7):
            newbox.piece=promotion("queen")
            info["promoted"]="queen"
        
        newbox.piece.notMoved=False
        moveDic.update(info)
        
def deadPiece(piece):
    if piece.color=="white":
        WhitePiece.whitePieces.remove(piece.piecetype)
        WhitePiece.deadWhite.append(piece.piecetype)
    else:
        BlackPiece.blackPieces.remove(piece.piecetype)
        BlackPiece.deadBlack.append(piece.piecetype)    
        
def printBoard():
    print(" ",end="")
    for i in range(8):
        print(" ",i,end=" ")
    print()    
    for i,row in enumerate(board):
        print(i,end=" ")
        for j,box in enumerate(row):
            if box.piece==None:
                print(" . ",end=" ")
            else:
                print(f"{box.piece.piecetype[0:2]}{box.piece.color[0]}",end=" ")
        print("\n")

'''
for i,row in enumerate(board):
    for j,box in enumerate(row):
        #print(box.color,box.row,box.col,end=" ")
        if box.piece!=None:
            print(box.piece.piece,box.piece.color)
        else:
            continue   
        if box.piece.piece=="king":
            print(box.piece.kingMoves(i,j))
        elif box.piece.piece=="queen":
            print(box.piece.queenMoves(i,j))
        elif box.piece.piece=="rook":
            print(box.piece.rookMoves(i,j))
        elif box.piece.piece=="bishop":
            print(box.piece.bishopMoves(i,j))
        elif box.piece.piece=="knight":
            print(box.piece.knightMoves(i,j))
        elif box.piece.piece=="pawn":
            print(box.piece.pawnMoves(i,j))
                '''
board=None
players=["white","black"]
def chessgame():
    numMoves=0
    global board
    board=createBoard()
    
    assignPieces(players[0],0)
    WhitePiece.king=(0,3)
    
    assignPieces(players[1],7)
    BlackPiece.king=(0,7)
    
    while True:
        printBoard()
        if players[numMoves%2]=="white":
            turn=WhitePiece
        else:
            turn=BlackPiece
            
        turncolor=turn.color    
        safe=isKingSafe(turn)
        if not safe:
            king=turn.king
            if showPossibleMoves(board[king[0]][king[1]]):
                print("Check!")
            else:
                print("Checkmate!")
                print(f"{turncolor.capitalize()} Wins!")
                break
                
        old=list(map(int,input("old: ").split()))
        oldbox=board[old[0]][old[1]]
        
        if oldbox.piece==None or not turncolor is oldbox.piece.color:
                continue
                
        new=list(map(int,input("next: ").split()))
        newbox=board[new[0]][new[1]]
        possMoves=showPossibleMoves(oldbox)
        movePiece(oldbox,newbox,possMoves)
            
        numMoves+=1
        gc.collect()
        
chessgame()