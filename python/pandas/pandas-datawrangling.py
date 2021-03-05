#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import pandas as pd
import numpy as np

#   Hierarchical Indexing
#   Enables you to have multiple (two or more) index levels on an axis. Somewhat abstractly, it provides a way for you to work with higher dimensional data in a lower dimensional form
data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1,2,3,1,3,1,2,2,3]])
print(data)
print()

#   With a hierarchically indexed object, so-called partial indexing is possible, enabling you to concisely select subsets of the data
print(data['b'])
print(data['b':'c'])
print(data[:, 2])
print()

print(data.loc['b'])
print(data.loc[['b', 'c']])
print(data.loc[:, 2])
print()

#   Hierarchical indexing plays an important role in reshaping data and group-based operations like forming a pivot table

#   data.unstack()
#       rearrange data into a DataFrame
print(data.unstack())
print()

#   data.stack()
#       inverse of unstack()
print(data.unstack().stack())
print()

#   With a DataFrame, either axis can have a hierarchical index
frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
#   The hierarchical levels can have names
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print()

#   With partial column indexing you can similarly select groups of columns:
print(frame['Ohio'])
print()

#   Creating a MultiIndex instance
_multi = pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])
print(_multi)
print()


#   Reordering and Sorting Levels

#   swaplevel(,i, j, axis)     
#       Takes two level numbers or names and returns a new object with the levels interchanged, that is, Swap levels i and j in a MultiIndex on a particular axis.
print(frame.swaplevel('key1', 'key2'))
print()

#   sort_index(axis[, level, ascending, inplace, kind, na_position, sort_remaining, ignore_index, key])
#       Sort object by labels (along an axis), only the values in a single level
print(frame.sort_index(level=1))
print()

print(frame.swaplevel(0, 1).sort_index(level=0))
print()


#   Summary Statistics by Level
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))
print()

#   Indexing with a DataFrame's columns
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd':[0,1,2,0,1,2,3]})
print(frame)
print()

#   set_index(keys, [drop=True, append=False, inplace=False, verify_integrity=False])
#       create a new DataFrame using one or more of its columns as the index
print(frame.set_index('d'))
frame2 = frame.set_index(['c', 'd'])
print(frame2)
print()

#   By default the columns are removed from the DataFrame, though you can leave them in
print(frame.set_index(['c', 'd'], drop=False))
print()

#   reset_index()
#       does the opposite of set_index; the hierarchical index levels are moved into the columns
print(frame2.reset_index())
print()


#   Combining and Merging Datasets
#   Data contained in pandas objects can be combined together in a number of ways
#           pandas.merge            connects rows based on one or more keys (like db join)
#           pandas.concat           concatenates or 'stacks' together objects along an axis
#           combine_first           enables splicing together overlapping data to fill missing values

#   Database-Style DataFrame Joins
#       Merge or join operations combine datasets by linking rows using one or more keys.
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print(df2)
print()

#   LINK: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
#   LINK: https://stackoverflow.com/questions/53645882/pandas-merging-101

#   merge(left, right[, how='inner', left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate])
#       Merge DataFrame or named Series objects with a database-style join.
#       merge is a many-to-one join. If column name is not specified, overlapping columns are used as keys. 
#               left            merge df LHS
#               right           merge df RHS
#               how             inner, outer, left, right (default=inner)
#               on              column names to join on, must be found in both tables, if not given use columns in both df
#               left_on         columns in left df to join on
#               right_on        columns in right df to join on
#               left_index      use index in left as join key (or keys if a multiindex)
#               right_index     use index in right as join key (or keys if a multiindex)
#               sort            sort merged data by join keys (default=True)
#               suffixes        tuple of string values to append to column names in case of overlap (default _x, _y)
#               copy            If False, avoid copying data into resulting structure, (default=True)
#               indicator       Add special column _merge that indicates source of each row,
#                               either 'left_only', 'right_only', or 'both'
print(pd.merge(df1, df2))
#   or
#>%     print(pd.merge(df1, df2, on='key'))
print()

#   By default merge does an 'inner' join; the keys in the result are the intersection, or the common set found in both tables
#   Different types of joins
#           inner           Use only the key combinations observed in both tables
#           outer           Use keys observed in either table
#           left            Use all key combinations found in the left table
#           right           Use all key combinations found in the right table
print(pd.merge(df1, df2, how='outer'))
print()

#   If the column names are different in each object, you can specify them separately
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
print()

#   Continue: 2021-03-04T23:51:02AEDT merge examples

#   To merge with multiple keys, pass a list of column names
#       think of the multiple keys as forming an array of tuples to be used as a single join key
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
print()

print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on='key1', suffixes=('_LHS', '_RHS')))
print()

#   Merging on index
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(pd.merge(left1, right1, left_on='key', right_index=True))
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))
print(left1.join(right1, on='key'))
print()


#   merging on index with hierachical index
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]], columns=['event1', 'event2'])
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))
print()

#   merging with both sides of index
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))
#   or
print(left2.join(right2, how='outer'))
print()

#    for simple index-on-index merges, you can pass a list of DataFrames to join as an alternative to using the more general concat function
another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]], index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
print(left2.join([right2, another]))
print(left2.join([right2, another], how='outer'))
print()


#   Concatenating Along an Axis

#   pd.concat(objs, [axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True])
#           objs            List or dict of pandas objects to be concatenated
#           axis            Axis to concatenate along
#           join            Either 'inner' or 'outer' union of index values
#           keys            values to associate with objects being concatenated
#           levels          Specific levels (unique values) to use for constructing a MultiIndex.
#           names           Names for created hiearchical levels if 'keys' and/or 'levels' passed
#           verify_index    Check new axis for duplicates, raise exception if found
#           ignore_index    Do not preserve indexes along concatenation axis (instead produce new range(len) index)

#   By default concat works along axis=0
arr = np.arange(12).reshape((3, 4))
print(np.concatenate([arr, arr], axis=0))
print(np.concatenate([arr, arr], axis=1))
print()

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

#   Calling concat with these objects in a list glues together the values and indexes, producing another Series
print(pd.concat([s1, s2, s3]))
#   Using axis=1 produces a dataframe
print(pd.concat([s1, s2, s3], axis=1))
print()

s4 = pd.concat([s1, s3])
print(s4)
print(pd.concat([s1, s4], axis=1, join='inner'))
print(pd.concat([s1, s4], axis=1))
print()

#   join_axes is deprecated
#>%   print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))
#   equivelent:
print(pd.concat([s1, s4], axis=1).reindex(['a', 'c', 'b', 'e']))
print()

#   A potential issue is that the concatenated pieces are not identifiable in the result. Sup‐ pose instead you wanted to create a hierarchical index on the concatenation axis. To do this, use the keys argument
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())
print()

#   In the case of combining Series along axis=1, the keys become the DataFrame col‐ umn headers
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
print()

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
#   or
print(pd.concat({'level1': df1, 'level2': df2}, axis=1))
print()

#   we can name the created axis levels with the names argument
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower']))
print()

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

#   preserves index values of LHS/RHS
print(pd.concat([df1, df2]))
#   ignores index values, new index values created for resulting array
print(pd.concat([df1, df2], ignore_index=True))
print()


#   Combining Data with Overlap
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

print(np.where(pd.isnull(a), b, a))
#   or
print(a.combine_first(b).values)

#   df.combine_first()
#       Update null elements with value in the same location in other. Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame. The row and column indexes of the resulting DataFrame will be the union of the two.
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan], 'b': [np.nan, 2., np.nan, 6.], 'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.], 'b': [np.nan, 3., 4., 6., 8.]})
print(df1.combine_first(df2))
print()


#   Reshaping with Hierarchical Indexing
#       Hierarchical indexing provides a consistent way to rearrange data in a DataFrame. There are two primary actions
#           stack           rotate or pivot from the columns in the data to the rows
#           unstack         pivot from the rows into the columns

data = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['Ohio', 'Colorado'], name='state'), columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)

#   Using the stack() method on this data pivots the columns into the rows, producing a Series
result = data.stack()
print(result)
print(data.stack(0))
print()

#   From a hierarchically indexed Series, you can rearrange the data back into a DataFrame with unstack()
print(result.unstack())

#   by default, the innermost level is tacked (or unstacked)
#       optionally, specify a level number or name:
print(result.unstack(0))
#   or
print(result.unstack('state'))
print()

#   Unstacking might introduce missing data if all of the values in the level aren’t found in each of the subgroups
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])

#   Stacking filters out missing data by default, (so the operation is more easily invertible)
print(data2.unstack().stack())
print(data2.unstack().stack(dropna=False))
print()

#   When you unstack in a DataFrame, the level unstacked becomes the lowest level in the result
df = pd.DataFrame({'left': result, 'right': result + 5}, columns=pd.Index(['left', 'right'], name='side'))
print(df)
print(df.unstack('state'))

#   When calling stack, we can indicate the name of the axis to stack
print(df.unstack('state').stack('side'))
print()


#   Pivoting 'Long' to 'Wide' format
#       long format - each row represents a single observation (minimal number of cols, maximum number of rows)

#   Combine year and quarter, and create row for 'realgdp', 'inf', and 'unemp' for each year-and-quater
data = pd.read_csv('data/macrodata.csv')
print(data)
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'start')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata)

#   df.pivot(index=None, columns=None, values=None)
#       Reshape data (produce a 'pivot' table) based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame.
#               index           column to use to make new frames index. If None, use existing index. Also accepts list of index names
#               column          column to use to make new frames columns. Also accepts list of column names
#               values          Column(s) to use for populating new frame’s values. If not specified, all remaining 
#                               columns will be used and the result will have hierarchically indexed columns.
pivoted = ldata.pivot('date', 'item', 'value')
#   or
pivoted = ldata.pivot(index='date', columns='item', values='value')
print(pivoted)
print()

#   pivot is equivalent to creating a hierarchical index using set_index followed by a call to unstack
#   Ongoing: 2021-03-05T23:12:34AEDT (if this is equivelent to pivot (above) -> where does 'value' come in?) <?>
unstacked = ldata.set_index(['date', 'item']).unstack('item')
print(unstacked)


#   If there is more than one data column being pivoted, adn no values argument is specified, the result is Hierachical columns
ldata['value2'] = np.random.randn(len(ldata))
pivoted = ldata.pivot('date', 'item')
print(pivoted)
print()


#   Pivoting 'Wide' to 'Long' format

#   df.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)   
#       inverse of pivot(). Merges multiple columns into one (producing df longer than input)
#       This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id_vars), while all other columns, considered measured variables (value_vars), are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'], 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df)
melted = pd.melt(df, ['key'])
print(melted)

reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped)

#   Since the result of pivot creates an index from the column used as the row labels, we may want to use reset_index to move the data back into a column
print(reshaped.reset_index())

#   You can also specify a subset of columns to use as value columns
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']))
print()

#   pandas.melt can be used without any group identifiers, too
print(pd.melt(df, value_vars=['A', 'B', 'C']))
print(pd.melt(df, value_vars=['key', 'A', 'B']))
print(pd.melt(df, value_vars=['key']))
print()


