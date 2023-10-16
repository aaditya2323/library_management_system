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



def call():
    b1=Books( )
    
    print ("Welcome to bookstore")
    print (""" 
                1. Add Books 
                2. Search Books
                3. show all books
                4. Exit
""")
    choice = int (input("Enter your Choice ::>"))
    if choice==1:
        b1.adddetails()
    
    elif choice==2:
        b1.searchbooks()
    
    elif choice==3:
         b1.showbooks()
    
    else:
        exit(0)
    
    
    
call()

    
    






        

