#Number Guessing Game project

import pandas as pd
import random
import os


file_name = "Game_data.csv"
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["player", "Choice", "attempts", "Score", "Result"])
    df.to_csv(file_name, index=False)

hard = random.randint(1, 500)
medium = random.randint(1, 100)
easy = random.randint(1, 50)


import time

welcome_text = """
🎯 Welcome to the Number Guessing Game! 🎯
Try to guess the number correctly.
Good luck!
"""

for char in welcome_text:
    print(char, end='', flush=True)
    time.sleep(0.05)

time.sleep(1)

player = input("enter your Name: ")


high_score=0
while True:

    choice=input("enter The Game you want easy(or'hard','medium', 'exit'): ").lower()

    if choice == "exit":
        print("Thank you for Playing")
        break

    if choice == "easy":
        max_attempts = 6
        attempts = 0
        win = False
        while True:
            r=int(input("enter number you guess"))
            attempts += 1
            if r > easy:
                print(" It's Too High! Try Again ")
            elif r < easy:
                print("It's Too Low ! try agin ")
            else:
                print(f"Congratulations you guess it in {attempts} attempts.")
                win = True
                break

            r3 = max_attempts - attempts
            print(f"Attempts left: {r3}\n")

            if attempts >= max_attempts:
                 print("your out of attempts Better luck next Time")
                 print(f"😢 The number was {easy}.")
                 break
                
            

        if win:
            score = max(0, max_attempts - attempts +1)
            result = "Win"
            print(result)
        else:
            score = 0
            result = "Lose"
            print(result)


        if score > high_score:
            high_score = score
        print(f"Your score: {score}")
        print(f"high score is: {high_score}")
        
        
        
        

                
           

            
    elif choice == "medium":
        max_attempts = 10
        attempts =0
        win = False
        while True:
            s=int(input("enter number you guess"))
            attempts += 1
            if s > medium:
                print(" It's Too High! Try Again ")
            elif s < medium:
                print("It's Too Low ! try agin ")
            else:
                print(f"Congratulations you guess it in {attempts} attempts.")
                win = True
                break
            r2 = max_attempts - attempts
            print(f"Attempts left: {r2}\n")

            if attempts >= max_attempts:
                 print("your out of attempts Better luck next Time")
                 print(f"😢 The number was {medium}.")
                 break

        if win:
            score = max(0, 100-(attempts *10))
            result = "Win"
        else:
            score = 0
            result = "Lose"

            
        if score > high_score:
            high_score = score
        print(f"Your score: {score}")
        print(f"high score is: {high_score}")
        
        

       
            
    elif choice == "hard":
        max_attempts = 6
        attempts = 0
        win = False
        while True:
            a=int(input("enter number you guess"))
            attempts += 1
            if a > hard:
                print(" It's Too High! Try Again ")
            elif a < hard:
                print("It's Too Low ! try agin ")
            else:
                print(f"Congratulations you guess it in {attempts} attempts.")
                win = True
                break

            r = max_attempts - attempts
            print(f"Attempts left: {r}\n")

            if attempts >= max_attempts:
                 print("your out of attempts Better luck next Time")
                 print(f"😢 The number was {hard}.")
                 break

        if win:
            score = max(0,max_attempts - attempts+1)
            result = "Win"
        else:
            score = 0
            result = "Lose"


        if score > high_score:
            high_score = score
        print(f"Your score: {score}")
        print(f"high score is: {high_score}")
        break



    if  choice != "exit":
        new_data = pd.DataFrame({
            "player": [player],
            "Choice": [choice],
            "Attempts": [attempts],
            "Score": [score],
            "Result": [result]
        })
        new_data.to_csv(file_name, mode='a', header=False, index=False)
        print("Game data saved")

        df = pd.read_csv(file_name)


        print("Your Game History:")
        player_data = df[df["player"] == player]
        print(player_data.tail(5))


        print("\n Top 5 players by Score: ")
        print(df.sort_values(by="Score", ascending=False).head(5))

            
        


            
        
        
        





