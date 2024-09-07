from datetime import datetime, timedelta

dateformat="%d-%m-%Y"
def daysdifference(date1,date2):
    date1=datetime.strptime(date1, dateformat)
    date2=datetime.strptime(date2, dateformat)
    return (actdate-expdate).days
    
class Book:
    def __init__(self, title, author, publication, category, isbn):
        self.title=title
        self.author=author
        self.publication=publication
        self.category=category
        self.timestramp=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.uniqueid=id(self)
        
    status="available"
    issuedby=None
    issuedate=None
    expectedreturn=None
    returndate=None
    history={}
    
class User:
    def __init__(self, username, password, role):
        self.username=username
        self.password=password
        self.role=role
        self.id=id(self)
        
    overdue=0
    issuedBooks=[]
    history={}
    
    def issueBook(self, book):
        book.status="issued"
        book.issuedby=self.userid
        book.issuedate=datetime.now().strftime("%d-%m-%Y")
        book.expectedreturn=book.issuedate+timedelta(days=7)
        self.issuedBooks.append(book)
        print("Book Issued Successfully")
        
    def returnBook(self, book):
        book.returndate=datetime.now().strftime("%d-%m-%Y")
        if daysdifference(book.expectedreturn,book.returndate)>0:
            self.overdue+=(daysdiff*10)
            
        self.history.update(book.__dict__)
        book.history.update(book.__dict__)
        
        self.issuedBooks.remove(book)
        book.status="available"
        book.issuedby=None
        book.issuedate=None
        book.expectedreturn=None
        book.returndate=None
        print("Book Returned Successfully")

class Library:
    books=[]    
    users=[]
    
    def addBook(self, book):
        self.books.append(book)
        print("Book Added Successfully")
        
    def deleteBook(self, book):
        self.books.remove(book)
        print("Book Deleted Successfully")
            
    def searchbyISBN(self, isbn):
        for bookavail in self.books:
            if bookavail.isbn==isbn:
                return bookavail
        return None
        
    def searchbyDetails(self, title, author):
        searched=[]
        for bookavail in self.books:
            if (title.lower()==bookavail.title.lower() or 
                author.lower()==bookavail.author.lower()):
                return bookavail
                
    def searchbyCategory(self, category):
        return [book for book in self.books if book.category==category]

library=Library()
user=User("anmol","anmol","Librarian")
library.users.append(user)

def login(username, password):
    for user in library.users:
        if user.username==username and user.password==password:
            return user
    return None
    
def createUser():
    username=input("Username: ")
    password=input("Password: ")
    role=input("Role: ")
    newuser=User(username, password, role)
    library.users.append(newuser)
    print("User Successfully added")
    print("User details:",newuser.__dict__)
    
def accessUser():
    userid=input("User ID: ")
    currentuser=None
    for user in library.users:
        if user.userid==userid:
            currentuser=user
            
    print(currentuser.__dict__)
    payfine=input("Want to pay all Overdue (Yes/No): ").lower()
    if payfine=="yes":
        currentuser.overdue=0

def libraryoper():
    print("Enter 1 to Add Book")
    print("Enter 2 to Search Book by ISBN")
    userin=int(input())
    if userin==1:
        title=input("Book Title: ")
        author=input("Author: ")
        publication=input("Publication: ")
        category=input("Category: ")
        isbn=input("ISBN: ")
        book=Book(title, author, publication, category, isbn)
        library.addBook(book)
        print("Book details:",book.__dict__)
        
    elif userin==2:
        isbn=int(input("ISBN: "))
        book=library.searchbyISBN(isbn)
        if book:
            print("Book details:", book.__dict__)
            print("Enter 1 to Modify Book details")
            print("Enter 2 to Delete Book")
            userin=int(input())
            if userin==1:
                book.title=input("Book Title: ")
                book.author=input("Author: ")
                book.publication=input("Publication: ")
                book.category=input("Category: ")
                print("Book details successfully")
                print("Book details:", book.__dict__)
            elif userin==2:
                library.deleteBook()
        else:
            print("Book not found")
    
username=input("Username: ")
password=input("Password: ")
user=login(username, password)
print("User details:", user.__dict__)

if user.role=="Librarian":
    print("Enter 1 to Create new user")
    print("Enter 2 to access user details and Overdue pay")
    print("Enter 3 to Perform Library Operations")
    print("Enter 4 to Issue or Return your Book")
    userin=int(input())
    
    if userin==1:
        print("Creating New User")
        createUser()
    elif userin==2:
        print("Accessing User Details")
        accessUser()
    elif userin==3:
        print("Performing Library Operations")
        libraryoper()
    elif userin==4:
        print("Your Books")
        

print("Enter 1 to Search book by Details")
print("Enter 2 to Search book by Category")
print("Enter 3 to Return book")
userin=int(input())
if userin==1:
    title=input("Title: ")
    author=input("Author: ")
    book=library.searchbyDetails(title, author)
    print("Book details:",book.__dict__)
    userin=input("Want to Issue book (Yes/No)").lower()
    if userin=="yes":
        user.issueBook(book)
    
elif userin==2:
    category=input("Category: ")
    book=library.searchbyCategory(category)
    print("Book details:",book.__dict__)
    userin=input("Want to Issue book (Yes/No)").lower()
    if userin=="yes":
        user.issueBook(book)
        
elif userin==3:
    issued=user.issuedBooks
    print("Issued Books:", issued)
    if issued:
        userin=int(input("Select Book to return:"))
        user.returnBook(user[0])
    else:
        print("No Issued Book")    