import csv
from user import User

class Books:
    Bookname=" "
    gener=" "
    Booknumber= " "
    price=" "
    

    def adddetails(self):
        u1=User
        if u1.loginuser(self):
             
            self.Bookname=input("enter book name::> ")
            self.gener=input("enter book gener::> ")
            self.Booknumber=input("enter book number::> ")
            self.price=input("enter book price::> ")

            with open("Books.csv", "a", newline="") as file:
                writer=csv.writer(file)
                writer.writerow([self.Bookname, self.gener, self.Booknumber, self.price])
            
            print("!!!--your details are added sucessfully--!!!")

    def searchbooks(self):
        self.Bookname=input("enter book name::>")
        with open("Books.csv", "r") as file:
            reader= csv.reader(file)
            for rows in reader:
                if self.Bookname==rows[0]:
                    print (f"""
                            Bookname={rows[0]}
                            gener={rows[1]}
                            booknumber={rows[2]}
                            price={rows[3]}                            
""")
                    print("____your details are saved as___")
                    
    def showbooks(self):
        with open("Books.csv", "r") as file:
            reader= csv.reader(file)
            for rows in reader:
                        print (f"""
                            Bookname={rows[0]}
                            gener={rows[1]}
                            booknumber={rows[2]}
                            price={rows[3]}
                 ------------------------------------------------
""")

    def deletebook(self):
        self.Bookname=input("enter a book name to delete::>")
        bookstokeep=[]
        with open("Books.csv" , "r") as file:
              reader=csv.reader(file)
              for rows in reader:
                   if self.Bookname==rows[0]:
                        continue
                   else:
                        bookstokeep.append(rows)
        with open("Books.csv", "w") as file:
             writer=csv.writer(file)
             writer.writerows(bookstokeep)
             print("!!Book deleted sucessfully!!")


    def editbook(self):
         self.Bookname=input("enter a book to edit::>")
         editbook=[]
         booktoremainsame=[]
         with open("Books.csv","r") as file:
              reader=csv.reader(file)
              for rows in reader:
                   if len(rows) >= 4 and self.Bookname == rows[0]:
                        self.Bookname=input("enter a new book name::>")
                        self.gener=input("enter book gener::>")
                        self.Booknumber=input("enter booknumber::>")
                        self.price=input("enter new price::>")
                        editbook=[(self.Bookname,self.gener,self.Booknumber,self.price)]

                   else:
                        booktoremainsame.append(rows)
        
         with open("books.csv","w") as file:
              writer=csv.writer(file)
              writer.writerows(booktoremainsame)
              writer.writerows(editbook)
              print("!!Book edited sucessfully!!")

                   
                      
def call():
    b1=Books( )
    
    print ("Welcome to bookstore")
    print (""" 
                1. Add Books 
                2. Search Books
                3. show all books
                4. edit
                5. delete
""")
    choice = int (input("Enter your Choice ::>"))
    if choice==1:
        b1.adddetails()
    
    elif choice==2:
        b1.searchbooks()
    
    elif choice==3:
         b1.showbooks()
    elif choice==4:
         b1.editbook()

    elif choice==5:
         b1.deletebook()
    
    
    else:
        exit(0)
    
    
    
call()

    
    






        

