"""
############## Data Visualization ##############

-- Data Visualization is a concept of graphical representation of data or information using visual elements like graphs, charts, and maps.
-- This representation helps us in understanding the patterns, trends, and outliers in the data and it makes data easily understandable and explainable.
-- With the increase in the volume of data, discovering the patterns in data has become challenging.
-- By making use of data visualization, a huge chunk of complex data can be displayed in a way that is easy to understand and is also appealing to the eyes.
-- In Data Visualization, plot is a basic structure for the graphical representation of data. Let us understand the plot and its components.


############## Plot ##############

-- A plot is the basic visualization element that helps to visualize the data.
-- To visualize(plot) the data, required is figure and axes objects.

>> Figure: The Figure is the top-level container that acts as the window or page on which everything is drawn.
            It can contain multiple independent subplots, multiple Axes, a title, a legend, etc.

>> Axes: The Axes are the area on which data is plotted. It can have labels or ticks associated with it.
            There can be multiple Axes in a figure. But a given Axes object can only be in one figure.

############## Anatomy of a plot ##############

A plot comprises several elements such as title, label, axes, legend etc., that adds more meaning to the visualization.

>> Title : The title is the name of the plot. By default, the title will be present at the top-center of the plot.
>> Axis : This consists of the X and Y axis which provide the horizontal and vertical coordinates of the data points.
>> Labels : The labels are used to name the X and Y axis with appropriate names respectively.
>> Legend : A legend is a set of key-value pairs that contains the list of plots and their respective labels.(Also to help identify which curve is for what purpose)

-- Apart from these, there are several customizations available for specific plots.




############# Introduction to Matplotlib #############


-- Matplotlib is one of the most basic and popular Python libraries used for data visualization.
-- It was developed for imitating the plotting capabilities of MATLAB.

-- matplotlib.pyplot :
is used for two-dimensional graphics in python programming.
It can be used in python shell, scripts, web application servers, and other graphical user interface toolkits.

-- Matplotlib uses libraries such as NumPy as a base for underlying operations.
-- Following are the various approaches to plotting in Matplotlib:
        -- MATLAB way of plotting using matplotlib.plyplot. It is simple to use
        -- Object-Oriented way of plotting for more control and customization

#importing the required packages
import matplotlib.pyplot as plt
import numpy as np

#creating two arrays
X=np.array([1,2,3,4,5])
Y=X**2

Now, let us plot the values using matplotlib.pyplot.

Syntax:
       plt.plot(x, y)
       x = data on the horizontal axis
       y = data on the vertical axis



-- matplotlib.pyplot is the simplest way of plotting.
-- It creates the default elements like Figure and Axes required and then plots the data.
-- This approach can be used to plot different kinds of graphs  like Line, Bar, Scatter plots, histogram etc.,





########## Object Oriented Interface in Matplotlib ############

-- We can also create the plotting elements using object Oriented approach.
-- The use of an object-oriented approach is recommended as it gives more control over customization of the plots.

-- Now, let us recreate the plot using object oriented approach following the below steps:

1.Creating a figure
2.Setting up the axes
3.Creating a plot using the axes object
4.Creating multiple plots using the same axes object
5.Setting up the title, label, and legend for a plot

----------------------------------------------------------------
#importing the required packages
import matplotlib.pyplot as plt
import numpy as np

#creating two arrays
X=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Y=X**X
A=X**5
B=X**5
C=X**5

plt.plot(X, Y)
plt.show()

---------------------------------------------------------------------------------

########## XY Axes ###########

#importing the required packages
import matplotlib.pyplot as plt
import numpy as np

#creating sample data for plotting
x = np.arange(1,16)    #1 … 15
y = x**2    #square of x values
z = (y/2)+40    #arithmetic operation applied to y values


# Creating an empty canvas or figure, to plot the values and visualize the plot.
fig = plt.figure()
#setting axes
ax = fig.add_axes([0,0,1,1])
#plotting the lines
ax.plot(x,y,color="g", label='line1' )
ax.plot(x,z,color="r", label='line2')
ax.set_title('Title of the Plot',fontsize=15)    #setting title
ax.set_xlabel('Label for X axis',fontsize=15)    # setting X label
ax.set_ylabel('Label for Y axis',fontsize=15)    # setting Y _label
ax.legend()    #adding legend
plt.show()

---------------------------------------------------------------------------------


###### Creating multiple axes #########

#importing the required packages
import matplotlib.pyplot as plt
import numpy as np
#creating sample data for plotting
x = np.arange(1,16)    #1 … 15
y = x**2    #square of x values
z = (y/2)+40    #arithmetic operation applied to y values

#creating an empty canvas/figure
fig = plt.figure(figsize=(8,5))                               #

#setting axes as [left, bottom, width, height]
ax1 = fig.add_axes([0,0,1,1])                                 #
ax2 = fig.add_axes([0.10,0.42,0.45,0.45])                     #

#plotting the lines

ax1.plot(x,y,color="g", label='line1' )
ax1.set_title('Title for Plot 1',fontsize=15)    # setting title
ax1.set_xlabel('Plot 1 - X axis',fontsize=15)    # setting X label
ax1.set_ylabel('Plot 1 - Y axis',fontsize=15)    # setting Y _label

ax2.plot(x,z,color="r", label='line2')
ax2.set_title('Title for Plot 2',fontsize=15)    # setting title
ax2.set_xlabel('Plot 2 - X axis',fontsize=15)    # setting X label
ax2.set_ylabel('Plot 2 - Y axis',fontsize=15)    # setting Y _label

ax1.legend()    #adding legend
ax2.legend()


-- Here, two plots are created using two different axes (ax1,ax2).
-- Though it seems like plot 2 is embedded in plot 1 due to the placement of the axes, plot 1 and plot 2 are completely different plots
-- and can only be accessed through ax1 and ax2 respectively.


---------------------------------------------------------------------------------


######### SUB PLOTS ############

-- The subplots method is used to create a common layout for multiple plots.
-- 'm x n' number of plots can be created using a subplot where m and n represent the number of rows and columns respectively.

-- Now, let us create a subplot that has 1 row and 2 columns.
-- A subplot is crested with two different plots aligned in 1 row and 2 columns.
-- In this plot, it is seen that the y_label of the second plot is overlapping with the first plot.
-- To avoid this, ‘fig.tight_layout()’ must be added.

Syntax:
       plt.subplots(nrows, ncols)

#creating sample data for plotting
x = np.arange(1,16)    #1 … 15
y = x**2    #square of x values
z = (y/2)+40    #arithmetic operation applied to y values

#initializing two axes for the subplot
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x,y,color="g", label='line1' )
ax1.set_title('Title for Plot 1',fontsize=15)    #setting title
ax1.set_xlabel('Plot 1 - X axis',fontsize=15)    # setting X label
ax1.set_ylabel('Plot 1 - Y axis',fontsize=15)    # setting Y _label

ax2.plot(x,z,color="r", label='line2')
ax2.set_title('Title for Plot 2',fontsize=15)    #setting title
ax2.set_xlabel('Plot 2 - X axis',fontsize=15)    # setting X label
ax2.set_ylabel('Plot 2 - Y axis',fontsize=15)    # setting Y _label

fig.tight_layout()


--------------------------------------------------------------------------------

#############  Types of plots  ###############

-- By now you know to import the data as a DataFrame, pre-process it, explore and gain insights from it using the Pandas library.
-- Deeper insights can be gained from the data by visualizing it using Matplotlib. Matplotlib has several kinds of plots. These plots can be used to get a visual understanding of various features present in the data, analyze them better, and present the data to the stakeholders.
-- So, let us visualize the data using Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\\INFY COURSE\\PythonForDataScienceCodeData\\auto_mpg.csv')
df.info()
#There are some null values observed in the ‘horsepower’ column. These needs to be replaced.
#replacing the null values in 'horsepower' with its mean value
df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)
df.info()




#### 1.BOX PLOT ####

-- boxplot gives a good indication of distribution of data about the median.
-- Boxplots are a standardized way of displaying the distribution of data based on the five-number summary i.e.,
   (“minimum”, first quartile (Q1)-25%, median-50%, third quartile (Q3)-75%, and “maximum”).

** IQR - first quartile (Q1)-25%, median-50%, third quartile (Q3)-75%

Syntax:
       ax.boxplot(data)  #ax represents axes



Problem Statement:
Some customers of XYZ Custom Cars are interested in the mileage range of the cars that are restored by the company.
They also want to compare the distribution of average mileage and city mileage (25% less than the average mileage).

Solution:
First, let us plot the average mileage ‘mpg’ from the data using a boxplot.
There is no data for city mileage, but city mileage is 25% less than the average mileage i.e. ‘mpg’. Next is to process the data for city mileage.
A new column  ‘city_mileage’ is created . Next, the distribution of the average mileage and city mileage has to be compared.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\\INFY COURSE\\PythonForDataScienceCodeData\\auto_mpg.csv')
df.info()
#There are some null values observed in the ‘horsepower’ column. These needs to be replaced.
#replacing the null values in 'horsepower' with its mean value
df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)
df.info()

#processing data for city mileage
df['city_mileage']=df['mpg']*0.75
print(df.head())

mpg_list = [df['mpg'],df['city_mileage']]           #Comparing avarage mpg and city mpg using boxplot

fig = plt.figure(figsize=[6,5])                     #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                     #setting axes
ax.set_title('Distribution of Average MPG vs City MPG')
ax.set_ylabel('Mileage per gallon')
ax.boxplot(mpg_list,widths = 0.5)                   #plotting box plot
fig.show()
plt.show()


#### 2.SCATTER PLOT ####

-- A scatter plot uses dots or markers to represent a value on the axes.
-- The scatter plot is one of the simplest plots which can accept both quantitative and qualitative values, with a wide variety of applications in primitive data analysis.
-- Several meaningful insights can be drawn from a scatter plot.
-- For example, identifying the type of correlation between variables before diving deeper into predictions.

-- STRONG POSITIVE CORRELATION : Left Bottom to Right Top ( positive slope)
-- NEGATIVE CORRELATION : Negative slope

Syntax:

       ax.scatter(x, y, marker)         # ax represents axes

       x = data on the horizontal axis
       y = data on the vertical axis
       marker = shape of data points (example 'o' for circles, 's' for squares etc.)

Problem Statement:
The engineers at XYZ Custom Cars want to infer the correlation between horsepower and mileage.
Solution:
First, let us plot a scatter plot for horsepower and mileage.

---->>> From the image it can be concluded that mileage and horsepower are negatively correlated to some extent.


fig = plt.figure(figsize=[10,5])                                #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                                 #setting axes
ax.scatter(df['horsepower'],df['mpg'])                          #plotting scatter plot
ax.set_title("Scatter plot of horsepower and mileage",fontsize=16)
ax.set_ylabel('Mileage per gallon',fontsize=12)
ax.set_xlabel('Horsepower',fontsize=12)
fig.show()


Secondly,Visualizing the correlation between mileage and horsepower based on the origin of the cars.

--->>>From the above plot , following are the insights:

1. Which country’s car has the highest mileage?
Ans: Japan

2. Which country’s car has the highest horsepower?
Ans: USA



from matplotlib import cm

fig = plt.figure(figsize=[12,5])                                                            #creating an empty canvas/figure

ax = fig.add_axes([0, 0, 1, 1])                                                             #setting axes
ax.set_title("Scatter plot of Horsepower and Mileage based on Origin",fontsize=16)
ax.set_ylabel('Mileage per gallon',fontsize=12)
ax.set_xlabel('Horsepower',fontsize=12)

origin_list = df["origin"].unique()
colors = cm.jet(np.linspace(0, 1, len(origin_list)))                                        #assigning different colors for each origin

for origin,color in zip(origin_list,colors):                                                # plotting based on the origin
    x = df[df["origin"] == origin]["horsepower"]
    y = df[df["origin"] == origin]["mpg"]
    ax.scatter(x,y,color = color,label=origin)
plt.legend()



#### 3.BAR CHART ####

-- A bar chart is a graph with rectangular bars that usually compare different categories.
-- Each bar represents a particular category. The length of the bar indicates the total number of values or items in that category.
-- The bar graphs can be plotted vertically or horizontally.

Syntax:

       ax.bar(x, height, width, bottom, align)                      #ax represents axes

       x = data on the horizontal axis
       height = height of the bar
       weight= weight of the bar. default:0.8
       bottom=Y coordinates of bar bases. default:0
       align = alignment of the bars to x coordinates. default value: 'center'

Problem Statement:
The engineers at XYZ Custom Cars want to know the number of cars released in each year.

Solution:
A bar graph can be created for this problem as shown below:


grouped_df = df.groupby(['model_year']).count()[['name']]           #Creating a grouped DataFrame according to model year
grouped_df.reset_index(inplace = True)
                                                                    #plotting the number of cars in each year
fig = plt.figure(figsize=[7,5])                                     #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                                     #setting axes
ax.set_title("Number of cars in each year",fontsize=16)
ax.set_ylabel('Number of cars',fontsize=12)
ax.set_xlabel('Model year',fontsize=12)

ax.bar(grouped_df['model_year'], grouped_df['name'])                #plotting bar graph
fig.show()
plt.show()


#### 4.Histogram ####

-- A histogram also represents data as rectangular bars. Unlike the bar graph, It is used for continuous data.
-- Each bar groups the numbers into intervals (bins) and the height of the bar is based on the number of values that fall into the corresponding intervals.
-- A histogram is ideally suited to obtain the frequency distribution of a given data .

Syntax:
       ax.hist(x, bins)                     #ax represents axes

       x = Input values. single array or sequence of arrays
       bins = int or sequence or str. If bins is integer, it defines the number of equal-width bins in the range.(no of bars of histograms)


Problem Statement:
The engineers at XYZ Custom Cars want to identify the distribution of horsepower.
Solution:
This can be done with the help of a histogram as follows:


fig = plt.figure(figsize=[8,6])                         #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                         #setting axes
ax.hist(df['horsepower'], bins=20)                      #plotting histogram
ax.set_title('Distribution of Horsepower',fontsize = 17)
ax.set_ylabel('Frequency',fontsize=12)
ax.set_xlabel('Horsepower',fontsize=12)
fig.show()
plt.show()


#### 4.Pie Chart ####

-- A Pie chart divides the entire dataset into distinct groups.
-- The chart consists of a circle split into pies and each pie represents a group.
-- The size of the pie is proportional to the number of items in each group compared to others.
-- The sum of the pies in a pie chart will always be 100%.

Syntax:
       ax.pie(x, labels)                                                #ax represents axes

       x = wedge size. one-dimensional array
       labels = sequence of strings providing the label for wedges


Problem Statement:
The management of XYZ Custom Cars has decided to open a new branch and is yet to decide the location.
They would like to concentrate more on the ‘origin’ of the cars to make a better decision.

Solution:
The details on origin of the cars and their numbers can be presented to the stakeholders visually for their easy understanding.
Let us visualize the data using a pie chart as follows:



pie_df = pd.DataFrame()                                     #creating a sub dataframe to plot the pie chart
pie_df['Count'] = df['origin'].value_counts()               #getting the count of ‘origin’ and assigning to the df
pie_df = pie_df.reset_index()                               #re-arranging the index
print(pie_df)
pie_df.rename(columns={'index':'Country'},inplace=True)     #re-naming the col (index to Country as after resetting the index is seperate column with serial number)
print(pie_df)

fig = plt.figure(figsize=[8,6])                             #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                             #setting axes
ax.set_title('Origin of the Cars')
ax.pie(pie_df['Count'], labels=pie_df['Country'])           #plotting pie chart
fig.show()
plt.show()


-- A basic Pie chart has been plotted using the ax.pie() function in matplotlib.
-- This plot could also be made visually appealing by customizing other parameters present in the ax.pie() function.

Following are the parameters:

explode         -   To get an elevated view for the selected pie.
colors          -   To customize the colors for the plot.
autopct         -   To add the percentage of the distribution in the pie chart.
shadow          -   To add shadow to the plot.
startangle      -   To change the starting angle of the pie chart.


fig = plt.figure(figsize=[8,6])
ax = fig.add_axes([0, 0, 1, 1])
explode = [0.05, 0, 0]
colors = ['yellowgreen', 'mediumaquamarine', 'khaki' ]
ax.set_title('Origin of the Cars')
ax.pie(pie_df['Count'], labels=pie_df['Country'],
        autopct='%0.1f%%',explode = explode,
        shadow = True, startangle = 250,
        colors = colors)
fig.show()


--->>> From the plot above, following are the insights:

1. Which will be the most suitable region to start a new branch?
Answer: USA

2. What is the percentage of cars produced from Europe?
Answer: 17.6%


"""



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm

df = pd.read_csv('D:\\INFY COURSE\\PythonForDataScienceCodeData\\auto_mpg.csv')
df.info()


#There are some null values observed in the ‘horsepower’ column. These needs to be replaced.
#replacing the null values in 'horsepower' with its mean value
df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)
df.info()


pie_df = pd.DataFrame()                                     #creating a sub dataframe to plot the pie chart
pie_df['Count'] = df['origin'].value_counts()               #getting the count of ‘origin’ and assigning to the df
pie_df = pie_df.reset_index()                               #re-arranging the index
print(pie_df)
pie_df.rename(columns={'index':'Country'},inplace=True)     #re-naming the col (index to Country as after resetting the index is seperate column with serial number)
print(pie_df)

fig = plt.figure(figsize=[8,6])                             #creating an empty canvas/figure
ax = fig.add_axes([0, 0, 1, 1])                             #setting axes
ax.set_title('Origin of the Cars')
ax.pie(pie_df['Count'], labels=pie_df['Country'])           #plotting pie chart
fig.show()
plt.show()
print(pie_df["Country"].apply(lambda x:x.split("a")[0]))


print(np.arange(15).reshape(5,3))

print(abs(200-865))