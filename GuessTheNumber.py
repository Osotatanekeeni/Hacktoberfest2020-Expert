import random
 
randNumber = random.randrange(1, 10)
print(randNumber)
 
guess = int(input("Enter a number between 1 and 10: "))
 
if guess == randNumber:
    print("Correct!")
elif guess < randNumber:
    print("Your guess is too low")
else:
    print("Your guess is too high")
