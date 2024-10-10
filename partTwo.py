import random # import the random number library so we can use the functions

RandomNumber = random.randint(1,10) # chooses a random number between 1 and 10
guess = int(input("guess the number i am thinking of between 1 and 10: "))
if guess > RandomNumber:
    print("too high")
elif guess < RandomNumber:
    print("too low")
else:
    print("you got it right!")

print("the number was " + str(RandomNumber))