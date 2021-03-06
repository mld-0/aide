import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#   See: OReilly Python for Data Analysis, Ch 9

#data = np.arange(10)
#print(data)
#
#plt.plot(data)
##plt.show()
#
##   Figures and Subplots
#fig = plt.figure()
#ax1 = fig.add_subplot(2, 2, 1)
#ax2 = fig.add_subplot(2, 2, 2)
#ax3 = fig.add_subplot(2, 2, 3)
#
#ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
#ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
#plt.plot(np.random.randn(50).cumsum(), 'k--')
##plt.show()
#
##>%     fig, axes = plt.subplots(2, 3)
#
##   plt.subplot()
##           nrows           number of rows
##           ncols           number of cols
##           sharex          all subplots should use the same x-axis ticks
##           sharey          all subplots should use the same y-axis ticks 
##           subplot_kw      dict of keywords passed to add_subplot call used to create each subplot
##           **fit_kw        additional keywords
#
#
##   Adjusting the spacing around subplots
##       subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
#
##   Data visualization with no inter-subplot spacing
#fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
#for i in range(2):
#    for j in range(2):
#        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
#plt.subplots_adjust(wspace=0, hspace=0)
##plt.show()
#
##   Colors, Markers, and Line Styles
##   to plot x versus y with green dashes
##>%     ax.plot(x, y, 'g--')
##   or
##>^     ax.plot(x, y, linestyle='--', color='g')
#
#
#from numpy.random import randn
#plt.plot(randn(30).cumsum(), 'ko--')
##   or
##>%     plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
##plt.show()
#
#
##   drawstyle
#data = np.random.randn(30).cumsum()
#plt.plot(data, 'k--', label='Default')
#plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
#plt.legend(loc='best')
##plt.show()
#
#
##   Ticks, Labels, and Legends
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#ax.plot(np.random.randn(1000).cumsum())
#ticks = ax.set_xticks([0, 250, 500, 750, 1000])
#labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
#ax.set_title('My first matplotlib plot')
#ax.set_xlabel('Stages')
##   or
#props = {
#    'title': 'My first matplotlib plot',
#    'xlabel': 'Stages'
#}
#ax.set(**props)
##plt.show()
#
#
##   Adding legends
#from numpy.random import randn
#fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)
#ax.plot(randn(1000).cumsum(), 'k', label='one')
#ax.plot(randn(1000).cumsum(), 'k--', label='two')
#ax.plot(randn(1000).cumsum(), 'k.', label='three')
#ax.legend(loc='best')
##plt.show()
#
#
##   Annotations and Drawing on a Subplot
#
##   You can add annotations and text using the text, arrow, and annotate functions. text draws text at given coordinates (x, y) on the plot with optional custom styling
##>%     ax.text(x, y, 'Hello world!', family='monospace', fontsize=10)
#
#from datetime import datetime
#
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#
#data = pd.read_csv('data/spx.csv', index_col=0, parse_dates=True)
#spx = data['SPX']
#
#spx.plot(ax=ax, style='k-')
#
#crisis_data = [
#        (datetime(2007, 10, 11), 'Peak of bull market'),
#        (datetime(2008, 3, 12), 'Bear Stearns Fails'),
#        (datetime(2008, 9, 15), 'Lehman Bankruptcy')
#]
#
#for date, label in crisis_data:
#    ax.annotate(label, xy=(date, spx.asof(date) + 75), xytext=(date, spx.asof(date) + 225), arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4), horizontalalignment='left', verticalalignment='top')
#
## Zoom in on 2007-2010
#ax.set_xlim(['1/1/2007', '1/1/2011'])
#ax.set_ylim([600, 1800])
#ax.set_title('Important dates in the 2008-2009 financial crisis')
#
##plt.show()
#
##   Drawing Shapes
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
#circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
#pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
#                   color='g', alpha=0.5)
#ax.add_patch(rect)
#ax.add_patch(circ)
#ax.add_patch(pgon)
#plt.show()


#   plt.savefig()
#           fname           filepath or python file-like object, format is inferred from extension
#           dpi
#           facecolor       figure background outside subplots <?>
#           edgecolor       <?>
#           format          explict file format to use (png, pdf, svg, ps, eps, ...)
#           bbox_inches     portion of the figure to save, if 'tight', attempt to trim empty space around figure

#   Saving plots to file. The file type is inferred from the file extension
#>%     plt.savefig('figpath.svg')

#   plot as a PNG with minimal whitespace around the plot and at 400 DPI
#>%     plt.savefig('figpath.png', dpi=400, bbox_inches='tight')

#   savefig doesn’t have to write to disk; it can also write to any file-like object, such as a BytesIO


#  matplotlib Configuration 
#       One way to modify the configuration programmatically from Python is to use the rc method; for example, to set the global default figure size to be 10 × 10, you could enter
#>%         plt.rc('figure', figsize=(10, 10))
#>%         font_options = {'family' : 'monospace', 'weight' : 'bold', 'size' :'small'} 
#   The first argument to rc is the component you wish to customize, such as 'figure', 'axes', 'xtick', 'ytick', 'grid', 'legend', or many others. After that can follow a sequence of keyword arguments indicating the new parameters. An easy way to write down the options in your program is as a dict
#>%         plt.rc('font', **font_options)


#   Plotting with Pandas

#   Line Plots
#       by default, plot() makes line plots
#s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
#s.plot()
#
#df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=['A', 'B', 'C', 'D'], index=np.arange(0, 100, 10))
#df.plot()
#
#plt.show()

#   Series.plot method arguments
#       label           label for plot legend
#       ax              matplotlib subject object to plot on, if nothing passed, activates subplot
#       style           style string (eg: 'ko--')
#       alpha           opacity
#       kind            options: area, bar, barh, density, hist, kde, line, pie
#       logy            use log y-axis 
#       use_index       use object index for tick labels
#       rot             rotation of tick labels (deg)
#       xticks          x-axis tick values
#       yticks          y-axis tick values
#       xlim            x-axis limits
#       ylim            y-axis limits
#       grid            display axis grid (Default <on>)

#   Dataframe specific plot arguments
#       subplots        plot each column in seperate subplot
#       sharex          if subplots, share x-axis ticks and limits
#       sharey          if subplots, share y-axis ticks and limits
#       figsize         tuple of figure size
#       title           plot title as string
#       legend          subplot legend (default=True)
#       sort_columns    plot columns in alphabetical order (default: use existing order)

#   Bar Plots
fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)
plt.show()

df = pd.DataFrame(np.random.rand(6, 4), index=['one', 'two', 'three', 'four', 'five', 'six'], columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.bar()
plt.show()

df.plot.barh(stacked=True, alpha=0.5)
plt.show()

#   A useful recipe for bar plots is to visualize a Series’s value frequency using 
#>%         value_counts: s.value_counts().plot.bar().

tips = pd.read_csv('data/tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]  # remove values outside range [2,5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)  # normalize to sum 1
party_pcts.plot.bar()
plt.show()

import seaborn as sns
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

sns.set(style="whitegrid")

#   Because there are multiple observations for each value in the day, the bars are the average value of tip_pct. The black lines drawn on the bars represent the 95% confidence interval
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')
plt.show()
#   seaborn.barplot has a hue option that enables us to split by an additional categorical value
sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h')
plt.show()


#   Histograms and Density Plots
tips['tip_pct'].plot.hist(bins=50)
plt.show()

tips['tip_pct'].plot.density()
plt.show()

#   Seaborn makes histograms and density plots even easier through its distplot method, which can plot both a histogram and a continuous density estimate simulta‐ neously. As an example, consider a bimodal distribution consisting of draws from two different standard normal distributions
comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
#   deprecated
#sns.distplot(values, bins=100, color='k')
sns.displot(values, bins=100, color='k')
#sns.histplot(values, bins=100, color='k')
plt.show()


#   Scatter or Point Plots
#   seaborn’s regplot method, which makes a scatter plot and fits a lin‐ ear regression line
macro = pd.read_csv('data/macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
sns.regplot(x='m1', y='unemp', data=trans_data)
plt.show()


#   In exploratory data analysis it’s helpful to be able to look at all the scatter plots among a group of variables; this is known as a pairs plot or scatter plot matrix. Making such a plot from scratch is a bit of work, so seaborn has a convenient pairplot function, which supports placing histograms or density estimates of each variable along the diagonal 
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
plt.show()


#    One way to vis‐ ualize data with many categorical variables is to use a facet grid. Seaborn has a useful built-in function factorplot that simplifies making many kinds of faceted plots
sns.catplot(x='day', y='tip_pct', hue='time', col='smoker', kind='bar', data=tips[tips.tip_pct < 1])
plt.show()

#   Instead of grouping by 'time' by different bar colors within a facet, we can also expand the facet grid by adding one row per time value
sns.catplot(x='day', y='tip_pct', row='time', col='smoker', kind='bar', data=tips[tips.tip_pct < 1])
plt.show()

#   factorplot supports other plot types that may be useful depending on what you are trying to display. For example, box plots (which show the median, quartiles, and out‐ liers) can be an effective visualization type
sns.factorplot(x='tip_pct', y='day', kind='box', data=tips[tips.tip_pct < 0.5])
plt.show()

