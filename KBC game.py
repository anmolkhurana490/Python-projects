import random
quesdic={
    1:{
        "value": 5000,
        "category": "GK",
        "ques": "What is the capital city of Australia?",
        "option": ("Sydney","Melbourne","Canberra","Brisbane"),
        "correct": "Canberra"
    },
    2:{
        "value": 10000,
        "category": "GK",
        "ques": "What is the capital city of France?",
        "option": ("Berlin","Paris","Rome","Madrid"),
        "correct": "Paris"
    },
    3:{
        "value": 20000,
        "category": "Science",
        "ques": "What is the chemical symbol for gold?",
        "option": ("Gd","Au","Ag","Fe"),
        "correct": "Au"
    },
    4:{
        "value": 40000,
        "category": "History",
        "ques": "Who was the first President of the United States?",
        "option": ("John Adams","Thomas Jefferson","George Washington","Abraham Lincoln"),
        "correct": "George Washington"
    },
    5:{
        "value": 80000,
        "category": "Technology",
        "ques": "What does CPU stand for?",
        "option": ("Central Processing Unit","Computer Personal Unit","Central Processor Unit","Central Personal Unit"),
        "correct": "Central Processing Unit"
    },
    6:{
        "value": 160000,
        "category": "Geography",
        "ques": "Which river is the longest in the world?",
        "option": ("Amazon","Nile","Yangtze","Mississippi"),
        "correct": "Nile"
    },
    7:{
        "value": 320000,
        "category": "Sports",
        "ques": "In which sport would you perform a slam dunk?",
        "option": ("Soccer","Basketball","Tennis","Golf"),
        "correct": "Basketball"
    },
    8:{
        "value": 640000,
        "category": "Movie",
        "ques": "Who directed the movie \"Inception\"?",
        "option": ("Christopher Nolan","Steven Spielberg","Quentin Tarantino","James Cameron"),
        "correct": "Christopher Nolan"
    },
    9:{
        "value": 1250000,
        "category": "Literature",
        "ques": "Who wrote the play \"Romeo and Juliet\"?",
        "option": ("William Shakespeare","Charles Dickens","Jane Austen","Mark Twain"),
        "correct": "William Shakespeare"
    },
    10:{
        "value": 2500000,
        "category": "Music",
        "ques": "Which instrument does Yo-Yo Ma play?",
        "option": ("Piano","Violin","Cello","Flute"),
        "correct": "Cello"
    },
    11:{
        "value": 5000000,
        "category": "Politics",
        "ques": "Who was the first President of the Indian National Congress?",
        "option": ("Jawaharlal Nehru","Dadabhai Naoroji","Sardar Patel","Bal Gangadhar Tilak"),
        "correct": "Dadabhai Naoroji"
    },
    12:{
        "value": 10000000,
        "category": "Mythology",
        "ques": "In Greek mythology, who is the god of thunder?",
        "option": ("Poseidon","Apollo","Zeus","Hermes"),
        "correct": "Zeus"
    },
}

prizelist=(5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000)
optionchar=["A","B","C","D"]

def question(quesnum):
    quesvalue=prizelist[quesnum]
    queslist=[]
    for key,ques in quesdic.items():
        if ques["value"]==quesvalue:
            queslist.append(key)
            
    chques=quesdic[random.choice(queslist)]
    
    statmt=chques["ques"]
    option=list(chques["option"])
    correct=chques["correct"]
    printques(quesvalue,statmt,option)
    while True:
        userin=input("Enter Option (A,B,C,D): ").upper()
        if userin in optionchar:
            lockedans=option[optionchar.index(userin)]
            break
        else:
            print("Option not valid")
            
    print(f"You Locked: ({userin}) {lockedans}")
    
    if lockedans==correct:
        print("Correct Answer!")
        return 1
    else:
        correctoption=optionchar[option.index(correct)]
        print(f"Correct Answer: ({correctoption}) {correct}")
        print("Wrong Answer!")
        return 0
    
def printques(value,statmt,option):
    print("Value:",value)
    print("Question:",statmt)
    for i in range(4):
        print(f"({optionchar[i]}) {option[i]}")
    print("")    
        
def kbcgame():
    print("Welcome to KBC Game".center(40))
    prizewon=0
    for i in range(len(prizelist)):
        print("")
        if question(i):
            prizewon=prizelist[i]
            print(f"You have won ₹{prizewon} till now")
        else:
            if prizewon>=320000:
                prizewon=320000
            else:
                prizewon=0
            print("")
            print(f"You have won total ₹{prizewon}!".center(40))
            print("Better luck next time!".center(40))
            break
    else:
        print("Congratulations! You have answered all answers correctly".center(20))
        print("You won ₹1 Crore".center(40))
        
kbcgame()    