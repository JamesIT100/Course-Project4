username = input("Enter username:  ")
pwd = input("Enter password:  ")
conf_pwd = input("Cofirm password:  ")
if conf_pwd == pwd:
    enc = conf_pwd.encode()

    hash1 = hashlib.md5(enc).hexdigest()
    with open("credentials.txt","w")as f:
        f.write("\n")
        f.write(hash1)
        f.close()
        print("You have registerd Successfully!")
else:
        print("Password is not same as above!\n")

def Login():

    username = input("Enter username:  ")
    username1 = "admin"
    pwd = input("Enter password:  ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt","r")as f:
        stored_username,stored_pwd = f.read().split
        f.close()
        if username1 == stored_username and auth_hash == stored_pwd:
            file1 = open("credentials.txt","r+")
            print(file1.read())
            if username == stored_username and auth_hash == stored_pwd:
                print("Logged in Successfully!")
            else:
                print("Login failed!\n")
while1:
print(".........login System.......")
print("1.signup")
print("2.Login")
print("3.Exit")
ch = int(input("Enter your choice:  "))
if ch == 1:
    signup()
elif ch == 2:
    Login()
elif ch == 3:
 break


else:
    print("Wrong choice!")
    username = input("Enter username:  ")
    pwd = input("Enter password:  ")
    conf_pwd = input("Conffirm password:  ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt","w")as f:
            f.write(username +"\n")
            f.write(hash1)
            f.close()
            print("You have registered Successfully!")
    else:
       print("Password is not same as above!\n")

def Login():
    username = input("Enter username:  ")
    username1 = "admin"
    pwd = input("Enter password:  ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open ("credentials.txt","r")as f:
        stored_username,stored_pwd = f.read().split("\n")
        f.close()
        if username1 == stored_username and auth_hash == stored_pwd:
            file1 = open ("credentials.txt","r")
            print(file1.read())
            if username == stored_username and auth_hash == stored_pwd:
                print("Logged in Successfully!")
        else:
            print("Login failed!\n")
            while1:
print(".........login system.....")
print("1.Signup")
print("2.Login")
print("3.Exit")
ch = int(input("Enter your choice"))
if ch == 1:
    signup()
elif ch == 2:
    login() 
elif ch == 3:

    break



else:
 print("Wrong choice!")