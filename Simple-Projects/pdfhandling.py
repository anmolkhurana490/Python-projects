import os
import PyPDF2

def printpdf(pdffile, pagenum):
	fl=open(pdffile, "rb")
	pdfReader=PyPDF2.PdfReader(fl).pages
	text=pdf[pagenum-1].extract_text()
	print(text)
	fl.close()
	
def rotatepdf(oldpdf, newpdf, rotation):
	old=open(oldpdf, "rb")
	pdfReader=PyPDF2.PdfReader(old)
	
	new=open(newpdf, "wb")
	pdfWriter=PyPDF2.PdfWriter()
	
	for page in pdfReader.pages:
		page.rotate(rotation)
		pdfWriter.add_page(page)
		
	pdfWriter.write(new)
	old.close()
	new.close()
	
def mergepdf(pdflist, outpdf):
	outfile=open(outpdf, "wb")
	pdfMerger=PyPDF2.PdfMerger()
	
	for pdf in pdflist:
		pdfMerger.append(pdf)
		
	pdfMerger.write(outfile)
	outfile.close()

def splitpdf(pdffile, splits):
    inputfile=open(pdffile, "rb")
    pdfReader=PyPDF2.PdfReader(inputfile)
    
    nametuple=os.path.splitext(pdffile)
    start=0
    
    for splitnum in range(len(splits)+1):
        pdfWriter=PyPDF2.PdfWriter()
        if splitnum<len(splits):
            end=splits[splitnum]-1
        else:
            end=len(pdfReader.pages)
            
        splitfile=nametuple[0]+str(splitnum)+".pdf"
        file=open(splitfile, "wb")
        for page in pdfReader.pages[start:end]:
            pdfWriter.add_page(page)
            
        pdfWriter.write(file)
        file.close()
        start=end
    
    inputfile.close()
    
def addwatermark(oldpdf, newpdf, wmpdf):
    old=open(oldpdf, "rb")
    pdfReader=PyPDF2.PdfReader(old)
    
    wm=open(wmpdf, "rb")
    wmReader=PyPDF2.PdfReader(wm)
    watermark=wmReader.pages[0]
    
    new=open(newpdf, "wb")
    pdfWriter=PyPDF2.PdfWriter(new)
    
    for page in pdfReader.pages:
        page.merge_page(watermark)
        pdfWriter.add_page(page)
        
    pdfWriter.write(new)
    new.close()
    wm.close()
    old.close()
    
while True:
    print("Enter 1 to print PDF page")
    print("Enter 2 to Rotate all PDF pages")
    print("Enter 3 to Merge multiple PDFs")
    print("Enter 4 to Split into multiple PDFs")
    print("Enter 5 to add Watermark to all PDF pages")
    
    userin=int(input("Enter input: "))
    
    if userin==1:
        path=input("Enter PDF path: ")
        page=int(input("Enter Page no.: "))
        printpdf(path, page)
    
    elif userin==2:
        oldfile=input("Enter original PDF path: ")
        newfile=input("Enter new PDF path: ")
        rotation=input("Rotation angle (clockwise): ")
        rotatepdf(oldfile, newfile, rotation)
        
    elif userin==3:
        pdflist=[]
        while True:
            oldfile=input("Enter PDF path: ")
            pdflist.append(oldfile)
            morepdf=input("Add more PDF (yes/no): ").lower()
            if morepdf!="yes":
                break
                
        newfile=input("Enter new PDF path: ")
        mergepdf(pdflist, newfile)
        
    elif userin==4:
        oldfile=input("Enter original PDF path: ")
        split=input("Enter pages from where to split, seperated by space: ").split()
        splitlist=list(map(int, split))
        splitpdf(oldfile, splitlist)
        
    elif userin==5:
        oldfile=input("Enter original PDF path: ")
        newfile=input("Enter new PDF path: ")
        wmpdf=input("Enter watermark PDF path: ")
        addwatermark(oldfile, newfile, wmpdf)
        