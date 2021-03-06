
#   Index operations with DataFrame
#       df[val]                     Select single column or sequence of columns, 
#                                   special cases: boolean array (filter rows), slice (slice rows), 
#                                   boolean DataFrame (set values per criterion)
#       df.loc[val]                 Select single row or subset of rows by label
#       df.loc[:, val]              Select single column or subset of columns by label
#       df.loc[[val1,]]              <?>
#       df.loc[val1, val2]          Select both row and column by label
#       df.iloc[where]              Select single row or subset of rows by integer position
#       df.iloc[:, where]           Select single column or subset of columns by integer position
#       df.iloc[where_i, where_j]   Select both rows and columns by integer position
#       df.at[label_i, label_j]     Select single scalar value by row and column label
#       df.iat[i, j]                Select single scalar valye by row and column positions (integers)
#       reindex()                   Select either rows or columns by labels
#       get_value(), set_value()    Select single valye by row and column label


#   Possible data inputs to DataFrame constructor
#       2d ndarray                                  Matrix of data 
#       dict of arrays, lists, or tuples            Each sequence becomes a column in the DataFrame, must all be same length
#       Numpy structured/record array               Treated as the 'dict-of-arrays' case
#       dict of Series                              Each value becomes a column, indexes from each Series are unioned together 
#                                                   to form the index if no explict index is passed
#       dict of dicts                               Each inner dict becomes a column, keys are unioned to form the row index
#       List of dicts or Series                     Each item becomes a row in the DataFrame, union of dict keys or series indexes
#                                                   becomes the DataFrame's column labels
#       list of list or tuples                      Treated as the 2d ndarray case
#       Another DataFrame                           DataFrame's indexes are used unless different ones are passed
#       NumPy MaskedArray                           Like the 2d ndarray case, except masked values become NA/missing in the result


#   Index methods and properties
#       append                  Concatenate with additional Index objects, producing a new Index 
#       difference              Compute set difference as an Index
#       intersection            Compute set intersection
#       union                   Compute set union
#       isin                    Compute boolean array indicating whether each value is contained in the passed collection 
#       delete                  Compute new Index with element at index i deleted
#       drop                    Compute new Index by deleting passed values
#       insert                  Compute new Index by inserting element at index i
#       is_monotonic            Returns True if each element is greater than or equal to the previous element 
#       is_unique               Returns True if the Index has no duplicate values
#       unique                  Compute the array of unique values in the Index

#   Flexible arithmetic methods (r<> methods have arguments flipped)
#       add, radd               addition (+)
#       sub, rsub               subtraction (-)
#       div, rdiv               division (/)
#       floordiv, rfloordiv     floor division (//)
#       mul, rmul               multiplication (*)
#       pow, rpow               exponentation (**)

#   shift(periods=1, freq=None, axis=0, fill_value=np.nan)
#       Shift index (with data) by desired number of periods with an optional time freq.  
#       (Leading and Lagging) data When shifting, missing data is introduced either at the start or the end of the time series
#>%             ts_percentshift = ts / ts.shift(1) - 1

#   df.reindex() 
#       Conform Series/DataFrame to new index with optional filling logic
#               index           new sequence to use as index
#               method          interpolation (fill) method, 'ffill' fills forward, 'bfill' fills backwards
#               fill_value      substitute value to use for introduced missing data
#               limit           when forward or back filling, maximum size gap (number of elements) to fill
#               tolerance       when forward or back filling, maximum size gap for indexact matches
#               level           Match simple Index on level of MultiIndex; otherwise select subset of.
#               copy            If True, always copy underlying data even if new index is equivalant to old index, 
#                               if False, do not copy the data when the indexes are independent

#   df.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)
#       Apply a function along an axis of the DataFrame
#           func            function to apply to each row
#           axis            axis along which function is applied (0=col, 1=row)
#           raw             True: pass function ndarray, False: pass function Series
#           result_type     (only axis=1) expand: turn list result into columns, 
#                           reduce: return Series, broadcast: retain origional index and column
#           args            position arguments to pass to func
#           kwds            additional keywords to pass to func

#   df.sort_index()

#   df.sort_values()

#   df.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None)
#           Provide rolling window calculations.


#   df.rank(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
#           Compute numerical data ranks (1 through n) along axis. By default, equal values are assigned a rank that is the average of the ranks of those values
#                   axis            0=rows, 1=cols
#                   method          average, min, max, first, dense


#   data.unstack(level=-1, fill_value=None)
#       Pivot a level of the (necessarily hierarchical) index labels
#       Returns a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.
#       If the index is not a MultiIndex, the output will be a Series (the analogue of stack when the columns are not a MultiIndex)
#       rearrange data into a DataFrame
#               level       level(s) of index to unstack, can pass level name (default=-1, last level)
#               fill_value  replace NaN with value if unstack produces missing values


#   data.stack(level=-1, dropna=True)
#       inverse of unstack()    
#       Stack the prescribed level(s) from columns to index.
#       Return a reshaped DataFrame or Series having a multi-level index with one or more new inner-most levels compared to the current DataFrame. The new inner-most levels are created by pivoting the columns of the current dataframe
#               level           Level(s) to stack from the column axis onto the index axis, defined as one index or label, 
#                               or a list of indices or labels
#               dropna          whether to drop rows in resulting Frame/Series with missing values

#   df.swaplevel(,i, j, axis)     
#       Takes two level numbers or names and returns a new object with the levels interchanged, that is, Swap levels i and j in a MultiIndex on a particular axis.


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


#   pd.concat(objs, [axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True])
#           objs            List or dict of pandas objects to be concatenated
#           axis            Axis to concatenate along
#           join            Either 'inner' or 'outer' union of index values
#           keys            values to associate with objects being concatenated
#           levels          Specific levels (unique values) to use for constructing a MultiIndex.
#           names           Names for created hiearchical levels if 'keys' and/or 'levels' passed
#           verify_index    Check new axis for duplicates, raise exception if found
#           ignore_index    Do not preserve indexes along concatenation axis (instead produce new range(len) index)


#   df.pivot(index=None, columns=None, values=None)
#       Reshape data (produce a 'pivot' table) based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame.
#       pivot is equivalent to creating a hierarchical index using set_index followed by a call to unstack
#               index           column to use to make new frames index. If None, use existing index. Also accepts list of index names
#               column          column to use to make new frames columns. Also accepts list of column names
#               values          Column(s) to use for populating new frame’s values. If not specified, all remaining 
#                               columns will be used and the result will have hierarchically indexed columns.


#   df.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)   
#       inverse of pivot(). Merges multiple columns into one (producing df longer than input)
#       This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id_vars), while all other columns, considered measured variables (value_vars), are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.


#   pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)
#           or
#   df.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)
#       Create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.
#               values              columns to aggregate
#               index               keys to group by on the pivot table index. If given, must be same length as data
#               columns             Keys to group by on the pivot table column. If given, must be same length as the data
#               aggfunc             Aggregation function or list of functions ('mean' by default); can be any function valid 
#                                   in a groupby context
#               fill_value          value to replace missing values in resulting pivot table
#               margins             add all row/columns (subtotals / grand-totals)
#               dropna              do not include columns whose entries are all NaN
#               margins_name        Name of the row/column that will contain 'margin' totals 
#               observed            If True: only show observed values for categorical groupers. If False: show all values 
#                                   for categorical groupers.



#   groupby methods
#           count               Number of non-NA values in group
#           sum                 Sum of non-NA values
#           mean                Mean of non-NA values
#           median              Median of non-NA values
#           std, var            standard deviation and variance
#           min, max            minimum and maximum non-NA values
#           prod                product of non-NA values
#           first, last         first and last non-NA values


#   DateTime Related:

#   date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)
#           Return a fixed frequency DatetimeIndex
#                   normalize           If True, Normalize start/end dates to midnight
#                   closed              None, left, right

#   Series.tz_localize(tz, axis=0, level=None, copy=True, ambigious='raise', nonexistance='raise')   
#       Localize tz-naive index of a Series or DataFrame to target time zone.
#               tz          str or tzinfo
#               axis        axis to localize
#               level       if axis is a multiindex, specify level, otherwise None

#   Series.tz_convert(tz)    
#       Conversion from one timezone to another 
#               tz          str, pytz.timezone, dateutil.tz.tzfile, or None


#   df.to_timestamp(freq=None, how='start', axis=0, copy=True)
#       Cast to DatetimeIndex of timestamps, at beginning of period.

#   Series.to_period(freq)
#      Cast to PeriodArray/Index at a particular frequency. Converts DatetimeArray/Index to PeriodArray/Index. 




