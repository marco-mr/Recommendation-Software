import pandas as pd
import random

class recommendation:
    csv = pd.read_csv("steam_dataset.csv")
    genres = csv["genres"].unique()

    def greet(self):
        print("------------------------------------------")
        print("| Welcome to the Steam game recommender! |")
        print("|    The top 100 games in each genre!    |")
        print("------------------------------------------")

    def get_user_input(self):
        print("\n-----Choose a genre!-----\n")
        print(self.genres)
        while True:
            genre_choice = input()

            if genre_choice.title() not in self.genres:
                print("Not a valid genre!")
                continue
            break
        self.get_user_action()

    def get_user_action(self):
        actions = {
            "Top 10": lambda: self.display_top_10(),
            "Range": lambda: self.display_range(),
            "Random": lambda: self.display_random(),
            "All": lambda: self.display_all()
        }

        print("\nHow would you like to display the games?")
        while True:
            action_choice = input("Top 10, Range, Random, All\n").title()
            if action_choice not in actions:
                print("Not a valid input!")
                continue
            break
        actions[action_choice]()


    def display_top_10(self):
        print("top 10")
    
    def display_range(self):
        print("range")

    def display_random(self):
        print("randon")

    def display_all(self):
        print("all")

    def start(self):
        self.greet()
        self.get_user_input()

software = recommendation()
software.start()