import random

user_name = input("What's your name?\n: ")
welcome_message = print(f"Hi {user_name} welcome to the simple guessing game")

print(
"""
Let's play the game!
Take a look at the boxes below:
-----------
|| || |_|
-----------
I have 3 boxes here.
Only one of them has a ball inside.
If you choose the box with the ball, you win!
"""
)

ball_position = random.randint(1,3)

user_answer = int(input("Which box do you choose? (1/2/3)\n: "))

if user_answer == ball_position:
    print(f"You win! The ball was inside box {ball_position}")
else:
    print(
    f"""
    You lose! The ball was inside box {ball_position}
    Repeat the program if you want to try again"""
)
