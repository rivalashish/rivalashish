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
is used for tow-dimensional graphics in python programming.
It can be used in python shell, scripts, web application servers, and other graphical user interface toolkits.

-- Matplotlib uses libraries such as NumPy as a base for underlying operations.
-- Following are the various approaches to plotting in Matplotlib:
        -- MATLAB way of plotting using matplotlib.plyplot. It is simple to use
        -- Object-Oriented way of plotting for more control and customization

"""