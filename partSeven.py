KeepPlaying = True
while KeepPlaying == True: # set the game to loop infinitely until the user chooses to exit
    
    #ask the user for the required input
    num1 = int(input("give me a number: "))
    num2 = int(input("give me another number: "))
    operator = input("type 'quit' to exit or give me an operator you can choose from + - * / ^ and %: ")
    result = 0

    match operator:
        case "quit":
            print("quitting the application")
            break
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                result = "ERROR you cannot divide by 0"
            else:
                result = num1 / num2
        case "^":
            result = num1 ** num2
        case "%":
            if num2 == 0:
                result = "ERROR you cannot divide by 0"
            else:
                result = num1 % num2
        case _:
            result = "ERROR INVALID INPUT"


    #display the result of the calculation
    print("you result is: "+ str(result))

