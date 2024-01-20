import os

n=1
def renamefile(dirpath):
    dirlist=os.listdir(dirpath)
    for dir1 in dirlist:
        path=dirpath+"/"+dir1
        global n
        dest=dirpath+"/"+str(n)+".png"
        if not os.path.exists(path):
        	continue
        elif os.path.isfile(path):
            pathtuple=os.path.splitext(path)
            if pathtuple[1]=='.png':
            	os.rename(path, dest)
            	n+=1
        else:
            renamefile(path)
    return
    
path="/storage/emulated/0"
renamefile(path)
print(n)
