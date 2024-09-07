import time
name=input("Your name: ")
ts=time.strftime("%H:%M:%S")
print(ts)
tsh=int(time.strftime("%H"))
if (tsh>=4 and tsh<10):
    greet="Morning"
elif (tsh>=10 and tsh<16):
    greet="Afternoon"
elif (tsh>=16 and tsh<20):    
    greet="Evening"
else:
    greet="Night"

print("Good "+greet+", "+name)    