# 2019 Oct 28 Homework 6

import pandas as pd

def price_check(price_min, price_max, file_name):
    df = pd.read_csv(file_name)
    criteria1 = df['price'] >= price_min
    criteria2 = df['price'] <= price_max
    criteria_all = criteria1 & criteria2
    print(df[criteria_all])

price_check(100, 150, "/Users/Aaron/Dropbox/Concordia/Continuing Education/CEBD 1100 - Intro to Python and Data Analysis/complete.csv" )