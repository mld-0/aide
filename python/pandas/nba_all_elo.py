#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import requests
import pandas as pd
import os
#   {{{2
#   LINK: https://realpython.com/pandas-python-explore-dataset/

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "data/nba_all_elo.csv"

#   Download data if file target_csv_path not found
if not os.path.isfile(target_csv_path):
    response = requests.get(download_url)
    response.raise_for_status()    # Check that the request was successful
    with open(target_csv_path, "wb") as f:
        f.write(response.content)
        print("Downloaded target_csv_path=(%s)" % str(target_csv_path))
else:
    print("Found target_csv_path=(%s)" % str(target_csv_path))


nba = pd.read_csv(target_csv_path)

print("type(nba)=(%s)" % str(type(nba)))
#   len(nba) returns number of rows
print("len(nba)=(%s)" % len(nba))
#   nba.shape gives tuple of (rows, cols)
print("nba.shape=(%s)" % str(nba.shape))

#   display all columns:
pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)

#   Set displayed decimal places to 2 
pd.set_option("display.precision", 2)

#   first five rows
print("nba.head()")
print(nba.head())

#   columns and their datatypes
print("nba.info()")
print(nba.info())

#   basic statistics
print("nba.describe()")
print(nba.describe())
print()

#   Exploratory data analysis
#       how oftern specific values occur in a column
print("team_id value_counts")
print(nba['team_id'].value_counts())
print("fran_id value_counts")
print(nba['fran_id'].value_counts())
print()

#   which teams are named 'Lakers'
print(nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts())
print()

#   When MNL games occured
print("MNL First and Last Games")
print(nba.loc[nba["team_id"] == "MNL", "date_game"].min())
print(nba.loc[nba["team_id"] == "MNL", "date_game"].max())
print(nba.loc[nba["team_id"] == "MNL", "date_game"].agg(("min", "max")))
print()

#   How many points 'BOS' scored during matches in dataset
print("BOS total points scored")
print(nba.loc[nba["team_id"] == "BOS", "pts"].sum())


#   Continue: 2021-02-11T20:56:03AEDT (see above) link, Using Pandas and Python to Explore Your Dataset, Series objects, DataFrame objects, Accessing elements, Querying dataset, grouping and aggregating data, manipulating columns, specifying datatypes, cleaning data, combining datasets, visualising dataframes


#   }}}1
