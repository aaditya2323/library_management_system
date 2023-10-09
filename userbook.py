import csv

class User:
    username=" "
    userid=" "
    userpassword=" "

    def __init__(self ,u_name,u_id,u_password) -> None:
        self.username=u_name
        self.userid=u_id
        self.userpassword=u_password

    def createUser(self):
        self.username=input("enter your user name::>")
        self.userid=input("enter your userid::>")
        self.userpassword=input("create your password ::> ")
        confirm_password=input("please confirm your password ::>  ")
        if self.userpassword==confirm_password:
            with open("User.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.username, self.userid, self.userpassword])
        else :
            print("Something Went Wrong :( !")


    def loginuser(self):
        self.username=input("enter your user name::>")
        self.userpassword=input("enter your password ::>")

        with open("User.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if self.username==row[0] and self.userpassword==row[2]:
                        print("login sucessfull")
                
                print("something went wrong")
def menu():
    u1=User(" "," "," ")
#    u1.loginuser()
    u1.createUser()


menu()





