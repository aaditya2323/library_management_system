import csv

class Books:
    Bookname=" "
    gener=" "
    Booknumber= " "
    price=" "

    def adddetails(self):
        self.Bookname=input("enter book name::> ")
        self.gener=input("enter book gener::> ")
        self.Booknumber=input("enter book number::> ")
        self.price=input("enter book price::> ")

        with open("Books.csv", "a", newline="") as file:
            writer=csv.writer(file)
            writer.writerow([self.Bookname, self.gener, self.Booknumber, self.price])

    # def serch


def call():
    b1=Books( )
    
    print ("Welcome to bookstore")
    print (""" 
                1. Add Books 
                2. Search Book
                3. Exit
""")
    choice = int (input("Enter your Choice ::>"))
    if choice==1:
        b1.adddetails()
    
    
    
call()

    
    



        
        
        


        

