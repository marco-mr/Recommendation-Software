import pandas as pd

class recommendation:
    csv = pd.read_csv("steam_dataset.csv")
    genres = csv["Genres"].unique()

    def start(self):
        print("------------------------------------------")
        print("| Welcome to the Steam game recommender! |")
        print("|      The top games in each genre!      |")
        print("------------------------------------------")
        self.get_user_input()

    def get_user_input(self):
        print("\n-----Choose a genre!-----\n")
        print(self.genres)
        while True:
            genre_choice = input()
            if genre_choice not in self.genres:
                print("Not a valid genre!")
                continue
            break
        self.games_with_genre = self.csv[self.csv["Genres"] == genre_choice]
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
                print("Not a valid input!\n")
                continue
            break
        actions[action_choice]()

    def display(self, games_to_display):
        print("\n")
        for _, row in games_to_display.iterrows():
            for col, value in row.items():
                print(f"{col}: {value}")
            print('-' * 50)
        self.reprompt()

    def display_top_10(self):
        self.display(self.games_with_genre.head(10))
    
    def display_range(self):
        print(f"There are {len(self.games_with_genre)} games available")
        start = int(input("Enter starting number: ")) - 1
        end = int(input("Enter end number: "))
        if start < 0 or end > len(self.games_with_genre) or start > end:
            print(f"Invalid range. Please enter a valid range (1 to {len(self.games_with_genre)} for start, and 1 to {len(self.games_with_genre)} for end).")
            self.display_range(self.games_with_genre)
        self.display(self.games_with_genre.iloc[start:end])
        
    def display_random(self):
        self.display(self.games_with_genre.sample(5))

    def display_all(self):
        with pd.option_context("display.max_rows", None):
            self.display(self.games_with_genre)

    def reprompt(self):
        reprompt = input("\nWould you like to: 1. Search for a different genre, 2. Display the current genre differently or 3. Quit?")
        actions = {
            "1": lambda: self.get_user_input(),
            "2": lambda: self.get_user_action(),
            "3": lambda: quit(),
        }

        if reprompt in actions:
            actions[reprompt]()
        print("Not a valid input!")
        self.reprompt()
        

recommendation_software = recommendation()
recommendation_software.start()