# Prompt the user to enter the number to be guessed
number = 2855255

# Prompt the user to enter their guess
guess = int(input("Enter your guess: "))

# Check if the guess is correct, too high, or too low
if guess > number:
    print("Too high!")
elif guess < number:
    print("Too low!")
else:
    print("Exactly right!")
