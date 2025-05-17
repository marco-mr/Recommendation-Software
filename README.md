# Recommendation-Software

Recommends the best rated games on Steam for each genre.

## Description

A simple recommendation system based on the user provided genre.
The dataset was modified by me, to only include the top 100 games (except sports and racing) for each genre based on their all time rating.
The program also provides aditional information per game: ex. price, developer, ...

The dataset included every single game released up until March 2025, anything released after is not included!
The steam_data_set_cleaner.py file is not needed but is included to show how I cleaned up the [Original Dataset](https://www.kaggle.com/datasets/artermiloff/steam-games-dataset) based on the needs of the project.

This is meant as a portfolio project, part of my computer science course on CodeCademy.

## Getting Started

### Dependencies

* Pandas - If not already installed please run: "pip install pandas" in the terminal

### Executing program

* To run the program you will need the recommendation-software.py and the steam_dataset.csv
* In the terminal move to the directory in which you have downloaded the project and enter
* On Windows:
```
python .\recommendation-software.py
```
* On Linux:
```
python3 .\recommendation-software.py
```

## Acknowledgments

* [Original Dataset](https://www.kaggle.com/datasets/artermiloff/steam-games-dataset)
* [CodeCademy](https://www.codecademy.com)
