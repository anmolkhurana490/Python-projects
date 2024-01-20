import tkinter as tk

root=tk.Tk()
root.geometry("600x400")
root.title("Calculator")

butlist=[["C","x","%","/"],
        [7,8,9,"*"],
        [4,5,6,"-"],
        [1,2,3,"+"],
        ["**",0,".","="]]
        
mainmenu=tk.Menu(root)
mainmenu.add_command(label="View")
mainmenu.add_command(label="Edit")
mainmenu.add_command(label="Help")
root.config(menu=mainmenu)

def click(event):
    global inputval, ansval
    button=event.widget.cget("text")
    inputtext=inputval.get()
    
    if not inputtext:
    	inputtext=""
    elif button=="C":
        inputval.set("")
        ansval.set(0)
    elif button=="x":
        inputval.set(inputtext[:-1])
    elif button=="=":
        if inputtext and inputtext[-1] in ["+","-","*","/","%","**"]:
            ans=eval(inputtext[:-1])
        else:
            ans=eval(inputtext)
        ansval.set(ans)
    elif button in ["+","-","*","/","%","**"]:
        if inputtext and inputtext[-1] in ["+","-","*","/","%","**"]:
            inputval.set(inputtext[:-1]+button)
        else:
            inputval.set(inputtext+button)
            
    if type(button)==int or button==".":
        inputval.set(inputtext+str(button))
        
    inputentry.update()
    anslabel.update()
    
screen=tk.Frame(root, bg="white")
screen.pack(fill=tk.BOTH)

inputval=tk.StringVar()
inputentry=tk.Label(screen, textvariable=inputval, font="lucida 15", bg="white", anchor="w")
inputentry.pack(fill=tk.X)

ansval=tk.StringVar()
anslabel=tk.Label(screen, textvariable=ansval, bg="white", anchor="e", font="lucida 15 bold")
anslabel.pack(fill=tk.X)

butFrame=tk.Frame(root)
butFrame.pack(fill=tk.BOTH, expand=True)

for i,row in enumerate(butlist):
    for j,button in enumerate(row):
        bcolor=None
        fcolor="black"
        if button=="=":
        	bcolor="red"
        	fcolor="white"
        elif button in ['C', 'x', '%', '/' ,'*', '+', '-']:
        	fcolor="red"
        	
        b1=tk.Button(butFrame, text=button, font="lucida 15 bold", bg=bcolor, fg=fcolor, activebackground="lightblue")
        b1.grid(row=i, column=j, sticky="news")
        b1.bind('<Button-1>', click)

for i in range(4):  # Assuming 4 columns
    butFrame.columnconfigure(i, weight=1)

for i in range(5):  # Assuming 5 rows
    butFrame.rowconfigure(i, weight=1)
  
root.mainloop()