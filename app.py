import random

try:
    while True:

        upper_bound = int(input("upper bound: "))
        lower_bound = int(input("lower bound: "))
        chance = int(input("how many chance you need? : "))

        hidden_number = random.randint(lower_bound, upper_bound)

        while chance != 0:
            print(f"chance left: {chance}")
            guess = int(input("guess the number: "))
            if guess == hidden_number:
                print("Correct, You've WON! CONGRATULATIONS!")
                break
            elif guess < hidden_number:
                print("guess too low, pick a higher number!")
            else:
                print("guess too high, pick a lower number!")
            chance -= 1

            if chance == 0:
                print(f"you lose, the number is {hidden_number}")

        play_again = input("do you want to play again (Y/N)? ")
        play_again.lower()

        if play_again != "y":
            break

        print("thanks for playing!")

except:
    print("please input number")
