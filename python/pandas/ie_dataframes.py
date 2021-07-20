#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#   {{{2
#   LINK: https://realpython.com/pandas-dataframe/

#   Pandas DataFrames are data structures that contain:
#       Data organized in two dimensions, rows and columns
#       Labels that correspond to the rows and columns

#   Creating DataFrame from dictionary of lists
data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
row_labels = [101, 102, 103, 104, 105, 106, 107]

#   Create dataframe
df = pd.DataFrame(data=data, index=row_labels)
print(type(df))
print(df)

#   (Optionally) Specify order of columns with columns parameter
#df = pd.DataFrame(data=data, index=row_labels, columns=['py-score', 'name', 'age', 'city'])

#   Dimensions of dataframe
print("len(df)=(%s)" % str(len(df)))
print("df.shape=(%s)" % str(df.shape))  # (rows, columns)
print("df.size=(%s)" % str(df.size))
print()

#   Get column labels (dataframe headings)
print(type(df.columns))
print(df.columns)
print()

#   Get row labels 
print(type(df.index))
print(df.index)
print()

#   Get 'city' row of the dataframe
print(type(df['city']))
print(df['city'])
#   alternatively:
# print(df.city)
print()

#   Get element of 'city' row by row_label
print(type(df['city'][102]))
print(df['city'][102])
print()

#   Get columns of row by row_label
print(type(df.loc[103]))
print(df.loc[103])
print()


#   Create pandas dataframe with list of dictionaries
l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]
print(pd.DataFrame(l))
print()

#   Create pandas dataframe with list of lists
#       explicitly specify column names
l = [[1, 2, 100],
     [2, 4, 100],
     [3, 8, 100]]
print(pd.DataFrame(l, columns=['x', 'y', 'z']))
print()

#   Create pandas dataframe with numpy array
#       if copy=False (which it is by default), the array is assigned to the dataframe, and modifying one changes the other
arr = np.array([[1, 2, 100], [2, 4, 100], [3, 8, 100]])
df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'], copy=False)
print(df_)
arr[0, 0] = 9
print(df_)
print()

#   Save dataframe to csv
df.to_csv('data/candidates.csv')
print(df)
print()

#   Update row indexes
df.index = np.arange(10, 17)
print(df)
print()

#   Convert dataframe to numpy array
print(type(df.to_numpy()))
print(df.to_numpy())
# print(type(df.values))
# print(df.values)
print()

#   Get Datatypes of each column
print(type(df.dtypes))
print(df.dtypes)
print()

#   Update datatype of column(s)
df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
print(df_.dtypes)
print()

#   Getting data with accessors
#       .loc[]          accepts the labels of rows and columns and returns Series or DataFrames. You can use 
#                       it to get entire rows or columns, as well as their parts. 
#                       inclusive stop index
#
#       .iloc[]         accepts the zero-based indices of rows and columns and returns Series or DataFrames. 
#                       You can use it to get entire rows or columns, or their parts. 
#                       exclusive stop index
#
#       .at[]           accepts the labels of rows and columns and returns a single data value.
#       .iat[]          accepts the zero-based indices of rows and columns and returns a single data value.
#   Don’t use tuples instead of lists or integer arrays to get ordinary rows or columns. Tuples are reserved for representing multiple dimensions in NumPy and Pandas, as well as hierarchical, or multi-level, indexing in Pandas.
print(df.loc[:, 'city'])
# print(df.iloc[:, 1])
print()
print(df.loc[11:15, ['name', 'city']])
# print(df.iloc[1:6, [0, 1]])
print()
print(df.iloc[1:6:2, 0])
# print(df.iloc[slice(1, 6, 2), 0])
# print(df.iloc[np.s_[1:6:2], 0])
# print(df.iloc[pd.IndexSlice[1:6:2], 0])
print()
print(df.at[12, 'name'])
# print(df.iat[2, 0])
print()

#   Setting data with accessors
print(df.loc[:, 'py-score'])
df.loc[:13, 'py-score'] = [40, 50, 60, 70]
df.loc[14:, 'py-score'] = 0
print(df['py-score'])

df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
print(df['py-score'])

#   Inserting Rows
john = pd.Series(data=['John', 'Boston', 34, 79], index=df.columns, name=17)
df = df.append(john)
print(df)
#   Deleting rows
#       by default df.drop() returns the modified dataframe. Pass 'inplace=True' to modify dataframe in place (and return None)
df = df.drop(labels=[17])
print(df)
print()

#   Inserting Columns
df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
df['total-score'] = 0.0
df.insert(loc=4, column='django-score', value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
print(df)
#   Delete Column
del df['total-score']
df = df.drop(labels='age', axis=1)
print(df)

#   Create new column as linear combination of existing columns
df['total'] = 0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
print(df)
print()

score = df.iloc[:, 2:5]
result = np.average(score, axis=1, weights=[0.4, 0.3, 0.3])
print(result)

#   Calculating 'total' column using np.average
del df['total']
df['total'] = np.average(df.iloc[:, 2:5], axis=1, weights=[0.4, 0.3, 0.3])
print(df)

#   Sorting a dataframe
#       sort by 'total' first, then by 'py-score'
#       sort_values() takes optional argument 'inplace=True' (False by default)
df = df.sort_values(by=['total', 'py-score'], ascending=[False, False])
print(df)
print()


#   Filtering data
filter_ = df['django-score'] >= 80
print(filter_)
print(df[filter_])
print()

print(df[(df['py-score'] >= 80) & (df['js-score'] >= 80)])
print()

print(df['django-score'].where(cond=df['django-score'] >= 80, other=0.0))
print()

print(df.describe())
print()


#   Handling missing data
df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})
print(df_)
print()
#   Calculating With Missing Data
#       Many Pandas methods omit nan values when performing calculations unless they are explicitly instructed not to:
print(df_.mean())
print(df_.mean(skipna=False))
print()

#   Fill missing data 
#   .fillna()           replace missing data with:
#       Specified values
#       The values above the missing value
#       The values below the missing value
#   .interpolate()      replace missing values with interpolated values
print(df_.fillna(value=0))
print(df_.fillna(method='ffill'))
print(df_.fillna(method='bfill'))
print(df_.interpolate())
#   Delete rows with missing data
print(df_.dropna())
print()

#   Iterate over pandas dataframe
#       .items() to iterate over columns
#       .iteritems() to iterate over columns
#       .iterrows() to iterate over rows
#       .itertuples() to iterate over rows and get named tuples

for col_label, col in df.iteritems():
    print(col_label, col, sep='\n', end='\n\n')
for row_label, row in df.iterrows():
    print(row_label, row, sep='\n', end='\n\n')
for row in df.loc[:, ['name', 'city', 'total']].itertuples():
    print(row)
print()


#   time series
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0, 9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1, 21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=len(temp_c), freq='H')
#   using time series as row labels
df_temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)

#   slice of df using datetimes
print(df_temp['2019-10-27 05':'2019-10-27 14'])
print()

#   resample() - mean, min, max temperature for each 6h interval
print(df_temp.resample(rule='6h'))
print(df_temp.resample(rule='6h').mean())
print(df_temp.resample(rule='6h').max())
print(df_temp.resample(rule='6h').min())
print()

#   rolling() - mean, max, min for rolling window
print(df_temp.rolling(window=3))
print(df_temp.rolling(window=3).mean())
print(df_temp.rolling(window=3).max())
print(df_temp.rolling(window=3).min())
print()

#   plot df_temp
df_temp.plot()
if not os.path.isdir('plots'):
    os.mkdir('plots')
df_temp.plot().get_figure().savefig('plots/temperatures.png')


#   }}}1
