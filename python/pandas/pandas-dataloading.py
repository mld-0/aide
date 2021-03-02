#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import pandas as pd
import numpy as np
#   {{{2
#   See: OReilly Python for Data Analysis 2nd Edition

#   Parsing Functions
#       read_csv
#       read_table
#       read_fwf 
#       read_clipboard
#       read_excel
#       read_hdf
#       read_html
#       read_json
#       read_msgpack
#       read_pickle
#       read_sas
#       read_sql
#       read_stata
#       read_feather

#   Reading basic csv (with headers)
df = pd.read_csv('data/ex1.csv')
#   or
df = pd.read_table('data/ex1.csv', sep=',')
print(df)
print()

#   Without headers
df = pd.read_csv('data/ex2.csv', header=None)
print(df)
#   Specify headers manually
df = pd.read_csv('data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df)
print()

#   Specify index column
names = ['a', 'b', 'c', 'd', 'message']
df = pd.read_csv('data/ex2.csv', names=names, index_col='message')
print(df)
print()

#   Multiple index columns
parsed = pd.read_csv('data/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)
print()

#   Using regex as delim
result = pd.read_table('data/ex3.txt', sep='\s+')
print(result)
print()

#   Skip specified rows (0-indexed)
df = pd.read_csv('data/ex4.csv', skiprows=[0, 2, 3])
print(df)
#   Comment character
df = pd.read_csv('data/ex4.csv', comment='#')
print(df)
print()

#   Specify values to be considered NA
result = pd.read_csv('data/ex5.csv', na_values=['NULL'])
print(result)
#   Specify values to be considered NA by column
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
result = pd.read_csv('data/ex5.csv', na_values=sentinels)
print(result)
print()

#   read_csv / read_table function arguments
#       path                    string indicating location / url
#       sep *or* delimiter      Chararacter sequence or regex to split fields
#       header                  row number to use as column names
#       index_col               Column numbers or names to use as row index
#       names                   List of column names for result (combined with header=None)
#       skiprows                Number of rows at beginning of file to ignore, or list of row numbers (0-indexed) to skip
#       na_values               List of values to replace in data with NA
#       comment                 character(s) to split comments off end of lines
#       parse_dates             If True, attempt to parse all columns. If column num/name, parse that column. If list 
#                               of columns, combine and parse
#       keep_date_col           If joining columns to parse date, keep the joined columns
#       converters              dict containing column number of name mapping to functions
#                               {'foo': f} applies function f to all values in column foo
#       dayfirst                when parsing ambigious dates, treat as international format
#       date_parser             function to use to parse dates
#       nrows                   number of rows to read from beginning of file
#       iterator                Return a TextParser object for reading file piecemeal <?>
#       chunksize               For iteration, size of chunks
#       skip_footer             number of lines to ignore at bottom of file
#       verbose                 print various parser output information
#       encoding                text encoding for unicode
#       squeeze                 if parsed data only contains one column, return a series
#       thousands               seperator for thousands (eg: ',' or '.')

#   Number of rows to be displayed
pd.options.display.max_rows = 10
result = pd.read_csv('data/ex6.csv')
print(result)
#   Number of rows to be read
result = pd.read_csv('data/ex6.csv', nrows=5)
print(result)
print()

#   chunksize
chunker = pd.read_csv('data/ex6.csv', chunksize=1000)
print(chunker)

#   value counts in the 'key' column
key_count = pd.Series([], dtype=int)
for loop_piece in chunker:
    key_count = key_count.add(loop_piece['key'].value_counts(), fill_value=0)
key_count = key_count.sort_values(ascending=False)
print(key_count)
print()

import sys

#   Writing data to text format
data = pd.read_csv('data/ex5.csv')
data.to_csv('data/out.csv')
#   Write to stdout, with custom seperator, and no index/header
data.to_csv(sys.stdout, sep='|', na_rep='NULL', index=False, header=False)
#   Write subset of columns
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
print()

dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('data/tseries.csv')

#   Reading a csv file manually
import csv
with open('data/ex7.csv') as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {k: v for k, v in zip(header, zip(*values))}
print(data_dict)
print()


#>%     class my_dialect(csv.Dialect): 
#>%         lineterminator = '\n' 
#>%         delimiter = ';'
#>%         quotechar = '"'
#>%         quoting = csv.QUOTE_MINIMAL
#>%     reader = csv.reader(f, dialect=my_dialect)

#   csvreader dialect options
#       delimiter                   one character seperator
#       lineterminator
#       quotechar
#       quoting
#       skipinitialspace            ignore whitespace after delim
#       doublequote                 how to handle quote char inside field
#       escapechar                  string to escape the delim

#   csv.writer       accepts same dialect and format options as csv.reader
#>%		with open('mydata.csv', 'w') as f:
#>%			writer = csv.writer(f, dialect=my_dialect) 
#>%			writer.writerow(('one', 'two', 'three')) 
#>%			writer.writerow(('1', '2', '3')) 
#>%			writer.writerow(('4', '5', '6')) 
#>%			writer.writerow(('7', '8', '9'))


#	Continue: 2021-03-01T15:35:14AEDT json data
import json
obj = """
    {"name": "Wes",
     "places_lived": ["United States", "Spain", "Germany"],
     "pet": null,
     "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                  {"name": "Katie", "age": 38,
                   "pets": ["Sixes", "Stache", "Cisco"]}]
} """

result = json.loads(obj)
print(result)
print()

#   xml and html
tables = pd.read_html('data/fdic_failed_bank_list.html', parse_dates=['Closing Date', 'Updated Date'])
failures = tables[0]
print(failures)
close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())
print()

from lxml import objectify
path = 'data/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()
data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR: 
    el_data = {}
for child in elt.getchildren(): 
    if child.tag in skip_fields:
        continue
    el_data[child.tag] = child.pyval
data.append(el_data)
perf = pd.DataFrame(data)
print(perf)


#   Binary formats
#   pandas objects all have a to_pickle method that writes the data to disk in pickle format
#       pickle is only recommended as a short-term storage format.
frame = pd.read_csv('data/ex1.csv')
frame.to_pickle('data/frame_pickle')
frame = pd.read_pickle('data/frame_pickle')
print(frame)
print()

#   HDF5    fails on MacOS, requires dependency 'tables' -> installable with miniconda, not with pyenv python
#>%     frame = pd.DataFrame({'a': np.random.randn(100)})
#>%     store = pd.HDFStore('mydata.h5')
#>%     store['obj1'] = frame
#>%     store['obj1_col'] = frame['a']
#>%     print(store)

#   requires:
#       pip isntall openpyxl xlrd
xlsx = pd.ExcelFile('data/ex1.xlsx')
frame = pd.read_excel(xlsx, 'Sheet1')
#   or
frame = pd.read_excel('data/ex1.xlsx', 'Sheet1')
print(frame)
print()

writer = pd.ExcelWriter('data/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()
#   or
frame.to_excel('data/ex2.xlsx')


#   Web APIs
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)
data = resp.json()
print(data[0]['title'])
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)
print()

#   Interacting with Databases
import sqlite3
query = """
     CREATE TABLE IF NOT EXISTS test
     (a VARCHAR(20), b VARCHAR(20),
      c REAL,        d INTEGER
     );"""
con = sqlite3.connect('data/mydata.sqlite')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6), ('Tallahassee', 'Florida', 2.6, 3), ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()
print(rows)

df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
print(df)
print()

import os
os.remove('data/mydata.sqlite')


#   }}}1
