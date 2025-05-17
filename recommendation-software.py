import pandas as pd

class Recommendation:
    def __init__(self):
        self.csv = pd.read_csv("steam_dataset.csv")
        self.genres = self.csv["Genres"].unique()
        self.genres_lower = {genre.lower(): genre for genre in self.genres}

    def start(self):
        print("------------------------------------------")
        print("| Welcome to the Steam game recommender! |")
        print("|      The top games in each genre!      |")
        print("------------------------------------------")
        self.get_user_input()

    def get_user_input(self):
        print("\n-----Choose a genre!-----\n")
        for genre in sorted(self.genres):
            print(f"- {genre}")

        while True:
            genre_choice = input("\nEnter a genre: ").strip().lower()
            if genre_choice not in self.genres_lower:
                print("Not a valid genre!")
                continue
            break
        selected_genre = self.genres_lower[genre_choice]
        self.games_with_genre = self.csv[self.csv["Genres"] == selected_genre]
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
        while True:
            try:
                start = int(input("Enter starting number: ")) - 1
                end = int(input("Enter end number: "))
                if start < 0 or end > len(self.games_with_genre) or start > end:
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid range. Please enter a valid range (1 to {len(self.games_with_genre)}).")
        self.display(self.games_with_genre.iloc[start:end])
        
    def display_random(self):
        self.display(self.games_with_genre.sample(5))

    def display_all(self):
        with pd.option_context("display.max_rows", None):
            self.display(self.games_with_genre)

    def reprompt(self):
        actions = {
            "1": lambda: self.get_user_input(),
            "2": lambda: self.get_user_action(),
            "3": lambda: SystemExit,
        }

        while True:
            reprompt = input("\nWould you like to: 1. Search for a different genre, 2. Display the current genre differently, or 3. Quit? ")
            if reprompt in actions:
                actions[reprompt]()
                break
            print("Not a valid input!\n")
        

if __name__ == "__main__":
    recommendation_software = Recommendation()
    recommendation_software.start()