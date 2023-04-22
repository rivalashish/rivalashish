"""

#############################  PANDAS  ############################

-- Pandas, built on top of Numpy when it comes to analysis and manipulation on tabular data.
-- Pandas is a popular library for data analysis built on top of the Python programming language.
     Pandas generally provide two data structures for manipulating data, They are:
        1.DataFrame
        2.Series


1.A DataFrame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
       -- A Pandas DataFrame will be created by loading the datasets from existing storage.
       -- Storage can be SQL Database, CSV file, an Excel file, etc.
       -- It can also be created from the lists, dictionary, and from a list of dictionaries.

2.Series represents a one-dimensional array of indexed data. It has two main components :
       -- An array of actual data.
       -- An associated array of indexes or data labels.
       -- The index is used to access individual data values. You can also get a column of a dataframe as a Series.
       -- You can think of a Pandas series as a 1-D dataframe.


# let us import the Pandas Library
import pandas as pd

Once you’ve imported pandas, you can then use the functions built in it to create and analyze data.



################ How to create a DataFrame out of a dictionary ################

-- Let us consider a dictionary 'x' with keys and values as shown below.
-- We then create a dataframe from the dictionary using the function pd.DataFrame(x)
-- The keys correspond to the column labels and the values or lists corresponding to the rows.



#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)


--------- Output:

   Name  ID       Department  Salary
0  Rose   1  Architect Group  100000
1  John   2   Software Group   80000
2  Jane   3      Design Team   50000
3  Mary   4   Infrastructure   60000



################ Column Selection:

To select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.
Let's Retrieve the data present in the ID column.

#Retrieving the "ID" column and assigning it to a variable x
y = df[['Department']]
print(y)

--------- Output:

        Department
0  Architect Group
1   Software Group
2      Design Team
3   Infrastructure


z = df[['Department','Salary','ID']]
print(z)

--------- Output:

        Department  Salary  ID
0  Architect Group  100000   1
1   Software Group   80000   2
2      Design Team   50000   3
3   Infrastructure   60000   4


print(type(x))
print(type(df))
print(type(y))

--------- Output:

<class 'dict'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>





################ To view the column as a series, just use one bracket:

# Get the Student column as a series Object

a = df['Department']
print(a)

--------- Output:

0     David
1    Samuel
2     Terry
3      Evan
Name: Student, dtype: object


print(type(a))

--------- Output:

<class 'pandas.core.series.Series'>



################ loc() and iloc() functions ################

  Student  Age Country            Course  Marks
0   David   27      UK            Python     85
1  Samuel   24  Canada   Data Structures     72
2   Terry   22   China  Machine Learning     89
3    Evan   32     USA   Web Development     76

-- loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select.
-- This method includes the last element of the range passed in it.

loc[row_label, column_label]


-- iloc() is an indexed-based selecting method which means that we have to pass integer index in the method to select a specific row/column.
-- This method does not include the last element of the range passed in it.

iloc[row_index, column_index]



df1.iloc[0, 0]
'David'

df1.iloc[0,2]
'UK'

df1.loc[0, 'Course']
'Python'



-------------- set_index() --------------

######### Let us create a new dataframe called 'df2' and assign 'df' to it. Now, let us set the "Name" column as an index column using the method set_index(). ########

df2=df1
df2=df2.set_index("Student")

#To display the first 5 rows of new dataframe
df2.head()

	     Age	Country	     Course	         Marks
Student
David	27	  UK	       Python	          85
Samuel	24	  Canada	   Data Structures	  72
Terry	22	  China	       Machine Learning	  89
Evan	32	  USA	       Web Development	  76


#Now, let us access the column using the name
df2.loc['David', 'Course']
'Python'






################## Slicing ##################

-- Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame.
-- To slice out a set of rows, you use this syntax: data[start:stop], start represents the index from where to consider,
and stop represents the index one step BEYOND the row you want to select. You can perform slicing using both the index and the name of the column.

NOTE: When slicing in pandas, the start bound is included in the output.

-- To select rows 0, 1, and 2 your code would look like this: df.iloc[0:3]     -- It means, to start at index 0 and select rows 0, 1, 2 up to but not including 3

NOTE: Labels must be found in the DataFrame or you will get a KeyError.

-- Indexing by labels(i.e. using loc()) differs from indexing by integers (i.e. using iloc())
-- With loc(), both the start bound and the stop bound are inclusive. When using loc(), integers can be used, but the integers refer to the index label and not the position.

For example, using loc() and select 1:4 will get a different result than using iloc() to select rows 1:4.



///1///  df1.iloc[0:2]   ---- 2 rows and all columns

(index) 	Student	    Age	  Country	  Course	        Marks
0	        David	    27	  UK	      Python	        85
1	        Samuel	    24	  Canada	  Data Structures	72

///2///  df1.iloc[0:2,0:3]   ---- 2 rows and 3 columns, it is as simple as x-axis(row) and y-axis(column).

(index) 	Student	    Age	  Country
0	        David	    27	  UK
1	        Samuel	    24	  Canada


///3///  df1.loc[0:2]   ---- 3 rows and all columns

row_label         Student	        Age	  Country	      Course	             Marks
0	              David	            27	  UK	          Python	              85
1	              Samuel	        24	  Canada	      Data Structures	      72
2	              Terry	            22	  China	          Machine Learning	      89

///4///  df2.loc['Samuel':'Terry', 'Age':'Course']   ---- here in df2 row_label is student itself ,ROW: From Samuel To Terry AND COLUMN:From Age TO Course

row_label	       Age	      Country	   Course
Student(row_label)
Samuel	           24	      Canada	   Data Structures
Terry	           22	      China	       Machine Learning




# Dependency needed to install file

!pip install xlrd
!pip install openpyxl


Let's go through the process to go from a comma separated values (.csv) file to a dataframe.
This variable csv_path stores the path of the .csv, that is used as an argument to the read_csv function.
The result is stored in the object df, this is a common short form used for a variable referring to a Pandas dataframe.

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
# Print first five rows of the dataframe
df.head()


We use the path of the excel file and the function read_excel. The result is a data frame as before:

# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
df.head()
x = df[['Length']]
x

"""
#
# import pandas as pd
#
#
# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)
# # Print first five rows of the dataframe
# print(df.head())
#
# xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
# df = pd.read_excel(xlsx_path)
# df.head()
# x = df[['Length']]
# print(x)
#
# y = df['Length']
# print(y)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)