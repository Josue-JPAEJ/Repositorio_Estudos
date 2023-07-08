import random


def guess(x: int):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        except Exception as err:
            print(err)

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!!")


def computer_guess(x: int):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too hight (H), too low (L), or correctly (C): ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid character.")


#guess(10)
computer_guess(10)
