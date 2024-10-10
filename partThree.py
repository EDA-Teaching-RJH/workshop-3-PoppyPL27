score = int(input("what did you score? ")) # takes the users score
grade = "" # set an empty variable for their grade

if score > 100 or score < 0: # check if they have inputed a valid score
    print("this is an invalid score") # tell them if they havent
else:
    if score > 90: 
        grade = "A" # they get an A if they scored over 90
    elif 80 <= score < 90:
        grade = "B" # they get an B if they scored over 80
    elif 70 <= score < 80:
        grade = "C" # they get an A if they scored over 70
    elif 60 <= score < 70:
        grade = "D" # they get an A if they scored over 60
    else:
        grade = "F" # if they got between 0 and 59 then they got an F
    
    print("your grade is: " + grade) # display their final grade
