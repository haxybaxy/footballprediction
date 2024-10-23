# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

matches = pd.read_csv("MATCH-RESULTS.csv")
season = pd.read_csv("SEASON-STATS.csv")

print(matches.head(5))
print(season.head(5))

shape_matches = matches.shape
shape_season = season.shape
dtype_matches = matches.dtypes
dtype_season = season.dtypes

print("Shape Matches: " + str(shape_matches))
print("Shape Seasins: " + str(shape_season))
print("Data Type Matches: " + str(dtype_matches))
print("Data Type Seasons: " + str(dtype_season))

classico_matches = matches[(matches["Home"].isin(["Barcelona","Real Madrid"])) & (matches["Away"].isin(["Barcelona","Real Madrid"]))]
print(classico_matches.head(5))


merged = pd.merge(season, matches, how="inner", on=["Competition_Name","Season_End_Year"])
corr = merged[["Gls", "xG_Expected","Poss","HomeGoals","AwayGoals"]].corr()
print(corr)


