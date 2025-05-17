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
        genre_choice = input("")

        if genre_choice.title() in self.genres:
            self.get_user_action()
        else:
            print("\nNot a valid genre!")
            self.get_user_input()

    def get_user_action(self):
        print("\nHow would you like to display the games?")
        action_choice = input("Top 10, Range, Random, All\n").title()
        if action_choice == "Top 10":
            print("Top 10")
        elif action_choice == "Range":
            print("Range")
        elif action_choice == "Random":
            print("Random")
        elif action_choice == "All":
            print("All")
        else:
            print("\nNot a valid action!")
            self.get_user_action()

    def start(self):
        self.greet()
        self.get_user_input()

software = recommendation()
software.start()