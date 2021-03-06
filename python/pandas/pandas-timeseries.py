#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytz
#   {{{2
#   See: OReilly Python for Data Analysis Ch11

#   Python datetime basics
from datetime import datetime
from datetime import timedelta

#   current time as python datetime
now = datetime.now()
print(f"now=({now})")
print(f"{now.year}, {now.month}, {now.day}, {now.hour}, {now.minute}, {now.second}, {now.microsecond}")
print()

#   datetime delta
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(f"delta=({delta})")
print(f"{delta.days}, {delta.seconds} {delta.microseconds}")  # delta contains only days, seconds, and microseconds
print(f"{delta.total_seconds()}")

print(timedelta(3))  # days
print(timedelta(3, 12345))  # days, seconds
print(timedelta(3, 12345, 24))  # days, seconds, microseconds

var = datetime(2011, 1, 7) + timedelta(7, 3208)  # add 7 days, 53mins, 28sec to datetime
print(var)
print()

#   String <-> datetime conversions

#   datetime.strptime requires datetime format to be specified
var_str = '2011-01-03'
var_dt = datetime.strptime(var_str, '%Y-%m-%d')
print(var_dt)
print()

#   Using dateutil.parser.parse (included with pandas)
from dateutil.parser import parse
var_dt = parse(var_str)
print(var_dt)
var_dt = parse('Jan 31, 1997 10:45 PM')
print(var_dt)
var_dt = parse('6/12/2011', dayfirst=True)
print(var_dt)
print()

#   Using pd.to_datetime
var_datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
var_dts = pd.to_datetime(var_datestrs)
print(var_dts)
var_dts = pd.to_datetime(var_datestrs + [None])  # handle 'missing' values
print(var_dts)
print(pd.isnull(var_dts))
print()

#   Pandas Time-Series
var_dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
var_values = np.random.randn(len(var_dates))

var_ts = pd.Series(var_values, index=var_dates)
print(var_ts)
print(var_ts.index)  # index values represented as DatetimeIndex
print(var_ts.index.dtype)  # pandas stores timestamps using numpy's datetime64 datatype

var_dt = var_dts[0]
print(var_dt)  # scalar values from a DatetimeIndex are pandas Timestamp objects
print()

#   operations between differently indexed time series automatically align on dates
print(var_ts + var_ts[::2])
print()

#   Time series behaves like any other pandas.Series when indexing and selecting data based on label
stamp = var_ts.index[2]
print(var_ts[stamp])

#   One can also pass a string that is interpretable as a date
print(var_ts['1/10/2011'])  # Note the Americanized date 
print(var_ts['20110110'])  
print(var_ts[datetime(2011, 1, 7)])  # slicing can also be done by datetime object
print()

#   slice with timestamps not contained in a time series to perform a range query
print(var_ts['1/6/2011':'1/11/2011'])
print(var_ts['2011-01-06':'2011-01-11'])
print(var_ts['2011-01-06':])
print()

#   truncate(before=None, after=None, axis=None, copy=True)
#       Truncate a Series or DataFrame before and after some index value. Slices a Series between two dates
print(var_ts.truncate(after='2011-09-01'))
print()

#   For longer time series, a year or only a year and month can be passed to easily select slices of data
longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(longer_ts['2001'])
print()
print(longer_ts['2001-05'])
print()

#   These operations also apply to DataFrames
var_dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
var_values = np.random.randn(len(var_dates), 4)
var_longDF = pd.DataFrame(var_values, index=var_dates, columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(var_longDF.loc['2001-05'])
print()

#   Time Series with duplicate indices
#       indexing into this time series will now either produce scalar values or slices depending on whether a timestamp is duplicated
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts)
print(dup_ts.is_unique)
grouped_dup_ts = dup_ts.groupby(level=0)  # groupby
print(grouped_dup_ts.mean())
print(grouped_dup_ts.count())
print()

#   Generic time series in pandas are assumed to be irregular; that is, they have no fixed frequency
#   Convert the sample time series to be fixed daily frequency by calling resample
print(var_ts.resample('D'))
print()


#   date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)
#           Return a fixed frequency DatetimeIndex
#                   normalize           If True, Normalize start/end dates to midnight
#                   closed              None, left, right

#   Generating Date Ranges
index = pd.date_range('2012-04-01', '2012-06-01')
index = pd.date_range(start='2012-04-01', periods=20)
index = pd.date_range(end='2012-06-01', periods=20)
index = pd.date_range('2000-01-01', '2000-12-01', freq='BM')  # BM = Buisness end-of-month
index = pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)  # normalize to midnight

#   Frequencies and Date Offsets
index = pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')
index = pd.date_range('2000-01-01', periods=10, freq='1h30min')
#   or
_freq = pd.tseries.offsets.Hour(1) + pd.tseries.offsets.Minute(30)
index = pd.date_range('2000-01-01', periods=10, freq=_freq)

#   Week-of-month
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')  # 3rd Friday of every month
print(rng)
print()

#   shift(periods=1, freq=None, axis=0, fill_value=np.nan)
#       Shift index (with data) by desired number of periods with an optional time freq.  
#       (Leading and Lagging) data When shifting, missing data is introduced either at the start or the end of the time series
ts = pd.Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts.shift(0))
print(ts.shift(2))
print(ts.shift(-2, fill_value=0))  # fill_value to use for newly introduced missing values

#   If freq is specified then the index values are shifted but the data is not realigned. That is, use freq if you would like to extend the index when shifting and preserve the original data.
print(ts.shift(2, freq='M'))
print(ts.shift(3, freq='D'))
print(ts.shift(1, freq='90T'))  # T stands for minutes
print()

#   A common use of shift is calculating percent changes in a time series
ts_percentshift = ts / ts.shift(1) - 1
print(ts_percentshift)
print()

#   Shifting dates with offsets
now = datetime(2011, 11, 17)
print(now + 3 * pd.tseries.offsets.Day())
print(now - pd.tseries.offsets.MonthEnd())
print(now + pd.tseries.offsets.MonthEnd())
print(now + pd.tseries.offsets.MonthEnd(2))
print(pd.tseries.offsets.MonthEnd().rollforward(now))
print(pd.tseries.offsets.MonthEnd().rollback(now))
print()

#   groupby date offsets
ts = pd.Series(np.random.randn(20), index=pd.date_range('1/15/2000', periods=20, freq='4d'))
print(ts.groupby(pd.tseries.offsets.MonthEnd().rollforward).mean())
#   or
print(ts.resample('M').mean())
print()


#   Time Zone handling
#   list of timezones
#>%     print(pytz.common_timezones)
#   By default, time series in pandas are time zone naive
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

#   Date ranges can be generated with a timezone set
pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='UTC')

#   Series.tz_localize(tz, axis=0, level=None, copy=True, ambigious='raise', nonexistance='raise')   
#       Localize tz-naive index of a Series or DataFrame to target time zone.
#               tz          str or tzinfo
#               axis        axis to localize
#               level       if axis is a multiindex, specify level, otherwise None
ts_utc = ts.tz_localize('UTC')
print(ts_utc)

#   Series.tz_convert(tz)    
#       Conversion from one timezone to another 
#               tz          str, pytz.timezone, dateutil.tz.tzfile, or None
ts_eastern = ts_utc.tz_convert('America/New_York')  # note the handling of DST 
print(ts_eastern)
print()
#   tz_localize and tz_convert are also instance methods on DatetimeIndex

#   Operations between timezones
#       If two time series with different time zones are combined, the result will be UTC. Since the timestamps are stored under the hood in UTC, this is a straightforward operation and requires no conversion to happen



#   Periods and Period Arithmetic
#       Periods represent timespans, like days, months, quarters, or years.
p = pd.Period(2007, freq='A-DEC')  # timespan from 2007-01-01 to 2007-12-31
print(p)
print(p + 5)
print(p - 2)

#   If two periods have the same frequency, their difference is the number of units between them
print(pd.Period('2014', freq='A-DEC') - p)

#   period_range(start=None, end=None, periods=None, freq=None, name=None)
#       Return a fixed frequency PeriodIndex. The day (calendar) is the default frequency.
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
print(rng)

#   The PeriodIndex class stores a sequence of periods and can serve as an axis index in any pandas data structure
print(pd.Series(np.random.randn(6), index=rng))

#   Using an array of strings
values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
print(index)
print()

#   Period frequency conversion
#       freq: W=weekly, Q=quarterly, A=annually
#       annual period into monthly period (at start/end of year)
p = pd.Period('2007', freq='A-DEC')
print(p)
print(p.asfreq('M', how='start'))
print(p.asfreq('M', how='end'))

#   For financial year
p = pd.Period('2007', freq='A-JUN')
print(p)
print(p.asfreq('M', how='start'))
print(p.asfreq('M', how='end'))
print()

#   Here, the annual periods are replaced with monthly periods corresponding to the first month falling within each annual period
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.asfreq('M', how='start'))

#   Quarter Period frequencies
#       get start and end of quarter by converting to daily frequency
p = pd.Period('2012Q4', freq='Q-JAN')
print(p.asfreq('D', 'start'))
print(p.asfreq('D', 'end'))

#   Period arithmatic
#       4pm on second last buisness day of the quarter
p4pm = (p.asfreq('B', 'end') - 1).asfreq('T', 'start') + 16*60
print(p4pm)
print()

#   Generate quarterly ranges using period_range()
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = pd.Series(np.arange(len(rng)), index=rng)
print(ts)
print()

#   Timestamp to Period conversion
#   
#   df.to_timestamp(freq=None, how='start', axis=0, copy=True)
#       Cast to DatetimeIndex of timestamps, at beginning of period.

#   Series.to_period(freq)
#      Cast to PeriodArray/Index at a particular frequency. Converts DatetimeArray/Index to PeriodArray/Index. 
rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
print(ts)
pts = ts.to_period()
print(pts)
print()

rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = pd.Series(np.random.randn(6), index=rng)
print(ts2)
pts = ts2.to_period()
print(pts)
ts2 = pts.to_timestamp()
print(ts2)
print()


#   Combining data fields to create period index
#>%     index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
#>%     data.index = index

#   df.resample(rule, axis=0, closed=None, label=None, convention='start', kind=None, loffset=None, base=None, on=None, level=None, origin='start_day', offset=None)
#       Resample time-series data. Convenience method for frequency conversion and resampling of time series. Object must have a datetime-like index (DatetimeIndex, PeriodIndex, or TimedeltaIndex), or pass datetime-like values to the on or level keyword.

#   Resampling and frequency conversion
#       Resampling refers to the process of converting a time series from one frequency to another. Aggregating higher frequency data to lower frequency is called downsam‐ pling, while converting lower frequency to higher frequency is called upsampling.
#       resample has a similar API to groupby; you call resample to group the data, then call an aggregation function
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())
print()

#   Downsampling (things to consider):
#       Which side of each interval is closed
#       How to label each aggregated bin, either with the start of the interval or the end
rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(len(rng)), index=rng)
print(ts)
#   Suppose you wanted to aggregate this data into five-minute chunks or bars by taking the sum of each group:
print(ts.resample('5min', closed='right').sum())
#>%     print(ts.resample('5min', closed='right', label='right', loffset='-1s').sum())  # label using right edge (deprecated)
#   or
_ts = ts.resample('5min', closed='right').sum()
_ts.index = _ts.index + pd.tseries.frequencies.to_offset('-1s')
print(_ts)
print()
#   ohlc()  open-high-low-close
print(ts.resample('5min').ohlc())
print()


#   Upsampling and Interpolation
#       When converting from a low frequency to a higher frequency, no aggregation is needed
frame = pd.DataFrame(np.random.randn(2, 4), index=pd.date_range('1/1/2000', periods=2, freq='W-WED'), columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(frame)
df_daily = frame.resample('D').asfreq()
print(df_daily)
#   ffil()  
print(frame.resample('D').ffill(limit=2))
print()

#   Resampling with periods
frame = pd.DataFrame(np.random.randn(24, 4), index=pd.period_range('1-2000', '12-2001', freq='M'), columns=['Colorado', 'Texas', 'New York', 'Ohio'])
annual_frame = frame.resample('A-DEC').mean()
print(annual_frame)
print(annual_frame.resample('Q-DEC').ffill())
print(annual_frame.resample('Q-DEC', convention='end').ffill())
print()

#   In downsampling, the target frequency must be a subperiod of the source frequency.
#   In upsampling, the target frequency must be a superperiod of the source frequency.


#   Moving Window Functions
#       An important class of array transformations used for time series operations are statis‐ tics and other functions evaluated over a sliding window or with exponentially decay‐ ing weights. This can be useful for smoothing noisy or gappy data. 
close_px_all = pd.read_csv('data/stock_px_2.csv', parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
print(close_px.AAPL.rolling(250).mean())
print(close_px.AAPL.rolling(250).std())
print()

#   df.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None)
#           Provide rolling window calculations.

#   The expression rolling(250) is similar in behavior to groupby, but instead of group‐ ing it creates an object that enables grouping over a 250-day sliding window.
close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot()
plt.show()

appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
appl_std250.plot()
plt.show()

#   df.expanding(min_periods=1, centre=None, axis=0)
#       Provide expanding transformations. The expanding mean starts the time window from the beginning of the time series and increases the size of the window until it encompasses the whole series.

expanding_mean = appl_std250.expanding().mean()
close_px.rolling(60).mean().plot(logy=True)
plt.show()

#   The rolling function also accepts a string indicating a fixed-size time offset rather than a set number of periods. Using this notation can be useful for irregular time series
print(close_px.rolling('20D').mean())
print()


#   Expodentially Weighted Functions
#       An alternative to using a static window size with equally weighted observations is to specify a constant decay factor to give more weight to more recent observations.

#   df.ewm(com=None, span=None, halflife=None, alpha=None, min_periods=0, adjust=True, ignore_na=False, axis=0, times=None)
#       Provide exponential weighted (EW) functions

#   comparing a 60-day moving average of Apple’s stock price with an EW moving average with span=60
aapl_px = close_px.AAPL['2006':'2007']
ma60 = aapl_px.rolling(30, min_periods=20).mean()
ewma60 = aapl_px.ewm(span=30).mean()
ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-', label='EW MA')
plt.legend()
plt.show()

#   Binary Moving Window Functions
#       Some statistical operators, like correlation and covariance, need to operate on two time series.

#   To have a look at this, we first compute the percent change for all of our time series of interest
spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()

#   df.corr(method='person', min_periods=1)
#       Compute pairwise correlation of columns, excluding NA/null values.

#   The corr aggregation function after we call rolling can then compute the rolling correlation with spx_rets
corr = returns['AAPL'].rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
plt.show()

#   Suppose you wanted to compute the correlation of the S&P 500 index with many stocks at once.
corr = returns.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
plt.show()


#   User-Defined Moving Window Functions
#       The apply method on rolling and related methods provides a means to apply an array function of your own devising over a moving window. The only requirement is that the function produce a single value (a reduction) from each piece of the array.

#   For example, while we can compute sample quantiles using rolling(...).quan tile(q), we might be interested in the percentile rank of a particular value over the sample.
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
plt.show()



#   }}}1
