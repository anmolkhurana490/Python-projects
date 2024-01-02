import random
import string

charlist=list(string.ascii_lowercase)
#list of alphabets from a-z

def encode(mess):
    wordlist=mess.split()
    code=""
    for word in wordlist:
        if len(word)<3:
            word=word[::-1]
        else:
            ch=word[0]
            word=word[1:]
            word+=ch
            for i in range(3):
                word=random.choice(charlist)+word
            for i in range(3):
                word+=random.choice(charlist)
                
        word+=" "
        code+=word
        
    return code.strip()
        
def decode(code):
    wordlist=code.split()
    mess=""
    for word in wordlist:
        if len(word)<3:
            word=word[::-1]
        else:
            for i in range(3):
                word=word[:len(word)-1]
            for i in range(3):
                word=word[1:]
            ch=word[len(word)-1]
            word=word[:len(word)-1]
            word=ch+word
                
        word+=" "
        mess+=word
        
    return mess.strip()
    

while True:
    mode=input("Want to Encode or Decode (en/de): ").lower()
    if mode=="en":
        mess=input("Enter message: ").lower()
        code=encode(mess)
        print("Your code:",code)
    elif mode=="de":
        code=input("Enter Code: ").lower()
        mess=decode(code)
        print("Your message:",mess)
    else:
        print("Input not valid!")
    print("")    