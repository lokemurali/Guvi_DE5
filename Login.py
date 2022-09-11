def Main():
    opt_val = True
    while opt_val == True:
        print("Welcome to Login Form")
        print("Enter Login/Register: ")
        option = input().upper();
        #print(option)
        if option == 'LOGIN':
            opt_val = False
            # Login Validation
            UserLogin() 
        elif option == 'REGISTER':
            opt_val = False
            # New User Registration
            user_registration() 
        else:
            print("Invalid Input, Try again")
    
    def user_registration():
    db = open(r"C:\Users\lokes\Documents\Guvi-DE5\register.txt", "r")
    Ex_Username = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        Ex_Username.append(a)
    verify_Reg = True
    ver_psw = 0;
    while(verify_Reg):
        UserName = input("Enter the email id or press enter to exit : ")
        
        if UserName == "":
            verify_Reg = False
        
        elif UserName.upper() in Ex_Username:
            print("Email already exist")
        else:
            usr_verify = validate_email(UserName)
            
            if usr_verify != True:
                print("Email Id is invalid, provide a valid emial id and try again");

            else:           
                pass1 = input("Enter the Password : ")
                pass2 = input("Confirm the Password : ")
                ver_psw = validate_pass(pass1,pass2)
                if ver_psw == 1:
                    print("Password doesn't match")
                elif ver_psw == 2:
                    print("Password should contain atleast 1 numeric,Caps,Small and Special Char, length should be min 6 to max 16 chars")
                elif ver_psw == 0:
                    verify_Reg = False
                    db = open("register.txt", "a")
                    db.write(UserName.upper()+", "+pass1+"\n")
                    print("User Registered Successfully!!")
                    print("Please login to proceed: ")
                    UserLogin()

 # Validate Email id (UserName Validation) #

def validate_email(user):
    
   #pat = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
   #pat = "^([a-zA-Z]{1})[a-zA-Z0-9-_.]+@[a-zA-z]+\.[a-zA-Z]{2,3}$"
    pattern = "^([a-zA-Z]{1})([\w\.\-]?)+@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
    if re.match(pattern,user):
        return True
    return False

 # Validate Password (Password Validation) #
def validate_pass(pass1,pass2):
    #pat = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    #pat = "^([a-zA-Z]{1})[a-zA-Z0-9-_.]+@[a-zA-z]+\.[a-zA-Z]{2,3}$"
    pattern = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[!-~]).{6,16}$"
    
    if(pass1 != pass2):
        return 1
    else:
        if re.match(pattern,pass1):
            return 0
        return 2
  ##########################################################################################
 
 def UserLogin():
    UserName = input("Enter the email: ")
    Password = input("Enter the Password: ")
    
    db = open(r"C:\Users\lokes\Documents\Guvi-DE5\register.txt", "r")
    user = []
    passs = []
    regis_info = {}
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        user.append(a.strip())
        passs.append(b.strip())
        regis_info = dict(zip(user,passs))
        
    #print ("user name : {} ; Password : {}".format(user,passs))
    #print("Login Info {}".format(regis_info))
    
    if UserName.upper() in regis_info:
        hashed = regis_info[UserName.upper()]
        if hashed == Password:
            print("Logged in Successfully!!")
            print("Welcome " + UserName)
        else:
            print("Invalid Password, Try again")
            UserLogin()
    else:
        print("invalid user email {}, do register".format(UserName))
        print("######### Welcome Registration Form ############## ")
        user_registration()
        
    
 ################## Calling Main Function #########################
import re
Main()
