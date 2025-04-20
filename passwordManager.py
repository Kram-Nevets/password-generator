from cryptography.fernet import Fernet #module that allows you to encrypt a string

"""
def create_key(): #creates a keyfile for your encryption
    key = Fernet.generate_key()

    with open("key.key","wb") as key_file:
        key_file.write(key)"""

def load_key(): # function used to decrypt the key

    file = open("key.key","rb")
    key = file.read()
    file.close()

    return key 




key = load_key()
fer = Fernet(key)

def view():

     with open("password.txt" , "r") as f:  #open a file, "a" means append "w" means write or overwrite the file "r" read the file
       for line in f.readlines():
           data = line.rstrip()
           user , passw = data.split("|") # returns the format from the file as a list form

           print("user: ",user,"| password: ",fer.decrypt(passw.encode()).decode())

    

def add():
        name = input("Account Name: ")
        password = input("Passsword: ")

        
        with open("password.txt" , "a") as f:  #open a file, "a" means append "w" means write or overwrite the file "r" read the file
            f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


         

while True:
    mode = input("Would like to add a new password or view existing passwords?Press Q to Quit: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode =="add":
        add()

    else: 
        print("invalid mode")
        continue



