import pandas as pd
import ast

# Original Data set from: https://www.kaggle.com/datasets/artermiloff/steam-games-dataset
# All credit to them

# import csv file 
df = pd.read_csv("games_march2025_cleaned.csv")

# select wanted columns
columns_to_keep = ['name', 'release_date', 'price', 'developers', 'categories', 'genres', 'pct_pos_total', 'pct_pos_recent', 'num_reviews_total']
clean_df = df[columns_to_keep]
clean_df = clean_df[clean_df['num_reviews_total'] >= 10000]

# convert string lists of categories and genres into normal lists with ast library
clean_df['genres'] = clean_df['genres'].apply(ast.literal_eval)
clean_df['categories'] = clean_df['categories'].apply(ast.literal_eval)

# Explode genres
clean_df = clean_df.explode('genres')

# Get top games per genre
# Sort data frame by the top 100 rated games
top_games_per_genre = clean_df.sort_values('pct_pos_total', ascending=False).groupby('genres').head(100)

# sort the games per genre
top_games_per_genre = top_games_per_genre.sort_values(by=['genres', 'pct_pos_total'], ascending=[True, False])

# write cleaned dataset into new csv
top_games_per_genre.to_csv('steam_dataset.csv', index=False)