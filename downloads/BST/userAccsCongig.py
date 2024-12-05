terminate = False    
global userlist
userlist = []

#Class declaration
class user:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return ("User Name: {} \nFull Name: {} \nEmail: {}".format(self.username, self.name, self.email))

#Method declaration
class useroperations:
    def insert():
        done = False
        while done != True:
            username = str(input("Username: "))
            if (username == "" or username == None):
                print("Username can NOT be blank!")
                continue
            if(useroperations.findUserByUsername(username) == "User not found!"):
                name = str(input("Full name: "))
                email = str(input("Email: "))
                newUser = user(username, name, email)
                i = 0
                while i < len(userlist):
                    if userlist[i].username > newUser.username:
                        break
                    i = i+1
                userlist.insert(i, newUser)
                print("Creation of user ", newUser.username, " successful.")
                done = True
            else:
                print("User Already exists!")
    

    def findUserByUsername(userCredentialsToBeSearched):        
        found = False
        for i in userlist:
            if i.username == userCredentialsToBeSearched:
                found = True
                return(i)
        if found == False:
            return("User not found!")
            
    def findUserByFullName(userCredentialsToBeSearched):        
        found = False
        for i in userlist:
            if i.name == userCredentialsToBeSearched:
                found = True
                return(i)
        if found == False:
            return("User not found!")
    
    def findUserByEmail(userCredentialsToBeSearched):        
        found = False
        for i in userlist:
            if i.email == userCredentialsToBeSearched:
                found = True
                return(i)
        if found == False:
            return("User not found!")

    def findSelector():
        while True:
            print("How do you want to search? \nUsername: U \nFull Name: F\nEmail: E")
            operation = str(input("Select an operation: "))
            match operation:
                case 'U':
                    print("\n--- SEARCH BY USERNAME ---")
                    userCredentialsToBeSearched = str(input("Enter the username please: "))
                    return(useroperations.findUserByUsername(userCredentialsToBeSearched))
                case 'F':
                    print("\n--- SEARCH BY FULL NAME ---")
                    userCredentialsToBeSearched = str(input("Enter the name please: "))
                    return(useroperations.findUserByFullName(userCredentialsToBeSearched))
                case 'E':
                    print("\n--- SEARCH BY EMAIL ---")
                    userCredentialsToBeSearched = str(input("Enter the Email please: "))
                    return(useroperations.findUserByEmail(userCredentialsToBeSearched))
                case _:
                    print("No such operation as ", operation)
                    continue
    def update():
        value = useroperations.findSelector()
        terminate = False
        while terminate != True:
            if value != "User not found!":
                while True:
                    toBeUbdated = str(input("What do you want to update? (U, F, E, Z to finish): "))
                    match toBeUbdated:
                        case 'U':
                            print("\n--- UPDATE USERNAME ---")
                            value.username = str(input("Enter new username: "))
                        case 'F':
                            print("\n--- UPDATE NAME ---")
                            value.name = str(input("Enter new name: "))
                        case 'E':
                            print("\n--- UPDATE Email ---")
                            value.email = str(input("Enter new Email: "))
                        case 'Z':
                            print("Terminating!")
                            terminate = True
                            break
                        case _:
                            print("No such operation as ", operation)
                            continue
            else:
                print("No such user!")
    
    def listing():
        print("Userame\t\t\tName\t\t\t\t\tEmail")
        for i in userlist:
            print("{}\t\t\t{}\t\t\t\t{}".format(i.username, i.name, i.email))


while terminate != True:
    print("\n\n1. Insert a new user \n2.Find an exsisting user\n3.Update an existing user\n4.List all users\n-1.Terminate Program")
    operation = int(input("Please choose an operation:"))
    match operation:
        case 1:
            print("\n--- INSERT OPERATION ---")
            useroperations.insert()
        case 2:
            print("\n--- FIND USER OPTION ---")
            print(useroperations.findSelector())
            pass
        case 3:
            print("--- UPDATE USER INFO ---")
            useroperations.update()
            pass
        case 4:
            print("---LIST USER INFO ---")
            useroperations.listing()
            pass
        case -1:
            terminate = True
            print("\n\n------TERMINATING------\n\n")
            break
