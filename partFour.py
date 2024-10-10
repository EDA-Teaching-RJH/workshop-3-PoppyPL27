username = "admin" #set valid username
password = "password123" # set valid password

UserInputUsername = input("username: ") # ask for users username
UserInputPassword = input("password: ") # ask for users password

if UserInputUsername == username and UserInputPassword == password: # check if both username and password are valid
    print("Acess granted. welcome " + username) # grant the user acess
else: # if the log in details are not correct in any way
    print("acess denied") # deny the user acess
