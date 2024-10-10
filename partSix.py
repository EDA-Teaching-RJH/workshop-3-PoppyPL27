age = int(input("what is your age? ")) # ask the user for their age
ticketprice = 0 # set ticket price initially to null

if age < 12 or age >= 65: # if they are a child
    ticketprice = 5 # childrens tickets cost 5 pounds
else: # if they are not a child
    Student = input("are you a student? ") # ask if they are a student
    if Student == "yes": # if they are a student
        ticketprice = 8 # student tickets cost 8 pounds
    else: # if they are not a student
        ticketprice = 10 # non student tickets cost 10 pounds

print("your ticket will cost £" + str(ticketprice)) # tel them how much their ticket will cost
