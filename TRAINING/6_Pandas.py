"""

#############################  PANDAS  ############################

https://pandas.pydata.org/docs/reference/frame.html

--Pandas is one of the most popular data wrangling and analysis tools because it:
        # has the capability to load huge sizes of data easily
        # provides us with extremely streamlined forms of data representation
        # can handle heterogenous data, has extensive set of data manipulation features and makes data flexible and customizable
-- Pandas, built on top of Numpy when it comes to analysis and manipulation on tabular data.
-- The steps involved to perform data analysis using Pandas are as follows:
    1.Read the Data.
    2.Explore the Data.
    3.Perform operations on Data
    4.Visualize the data.
    5.Generate insights
-- Pandas is a popular library for data analysis built on top of the Python programming language.
     Pandas generally provide two data structures for manipulating data, They are:
        1.DataFrame
        2.Series


----------- ######### --------------

1.The first step is to read the data. There are multiple formats in which data can be obtained such as '.csv', '.json', '.xlsx' etc. JSON(javascript object notation)
2.Exploring data helps to:
        -- know the shape(number of rows and columns) of the data
        -- understand the nature of the data by obtaining subsets of the data
        -- identify missing values and treat them accordingly
        -- get insights about the data using descriptive statistics
3.Performing operations on the data :
  Some of the operations supported by pandas for data manipulation are as follows:
        -- Grouping operations
        -- Sorting operations
        -- Masking operations
        -- Merging operations
        -- Concatenating operations
4.Visualizing data
  The next step is to visualize the data to get a clear picture of various relationships among the data. The following plots can help visualize the data:
        -- Scatter plot
        -- Box plot
        -- Bar plot
        -- Histogram and many more
5.Generating Insights
  All the above steps help generating insights about our data.


----------- ######### --------------

1.A DataFrame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
       -- A Pandas DataFrame will be created by loading the datasets from existing storage.
       -- Storage can be SQL Database, CSV file, an Excel file, etc.
       -- It can also be created from the lists, dictionary, and from a list of dictionaries.

2.Series represents a one-dimensional array of indexed data. It has two main components :
       -- An array of actual data.
       -- An associated array of indexes or data labels.
       -- The index is used to access individual data values. You can also get a column of a dataframe as a Series.
       -- You can think of a Pandas series as a 1-D dataframe.

----------- ######### --------------

# let us import the Pandas Library
import pandas as pd

Once you’ve imported pandas, you can then use the functions built in it to create and analyze data.


############# Pandas Series object #############

-- Series is one dimensional labelled array. It supports different datatypes like integer, float, string etc.

Syntax: pd.Series(data, index, dtype)

series = pd.Series(data = [78, 92, 36, 64, 89])
print(series)                                # provides the values.             -->>          0    78
                                                                                            # 1    92
                                                                                            # 2    36
                                                                                            # 3    64
                                                                                            # 4    89
                                                                                            # dtype: int64
print(series.values)                         # provides the values.              -->>     [78 92 36 64 89]
print(series.index)                          # provides the index.              -->>     RangeIndex(start=0, stop=5, step=1)
print(series[1])                             # Accesing values based on index   -->>     92
print(series[1:3])                           # Slicing                          -->>              1    92
                                                                                                # 2    36
                                                                                                # dtype: int64

############## Custom index in series ##############

-- By default, series creates an integer index. The custom index can also be defined.
-- A Pandas series can be created using the following syntax:

data = pd.Series(data = [700000, 800000, 1600000, 1800000, 30000000], index = ['Swift', 'Jazz', 'Civic', 'Altis', 'Gallardo'])

print(data)                                                                         -->>        # Swift       700000
                                                                                                # Jazz        800000
                                                                                                # Civic       1600000
                                                                                                # Altis       1800000
                                                                                                # Gallardo    30000000
                                                                                                # dtype: int64

print(data['Swift'])                             # Accesing values based on index   -->>     92

print(data['Jazz':'Altis'])                # Slicing (here both strt and end taken) -->>        # Jazz        800000
                                                                                                # Civic       1600000
                                                                                                # Altis       1800000




#casting the dictionary to a Series
x_dict -- dictionary , where index as key and value as values
series = pd.Series(x_dict)



-- A series gives a useful way to view and manipulate one dimensional data.
-- But when data is present in rows and columns, it becomes necessary to make use of the Pandas DataFrame object.
-- A DataFrame is a collection of series where each series represents a column from a table.


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

#To display the last 5 rows of new dataframe
df2.tail()

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


-- Let's go through the process to go from a comma separated values (.csv) file to a dataframe.
-- This variable csv_path stores the path of the .csv, that is used as an argument to the read_csv function.
-- The result is stored in the object df, this is a common short form used for a variable referring to a Pandas dataframe.

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



### Below is an example of creating a DataFrame from a json file.

data_json = pd.read_json('example.json',)
data_json.head()

#--->>> Pandas can read a variety of files.
        For example, a table of fixed width formatted lines (read_fwf), excel sheets (read_excel), html files (read_html), json files (read_json) etc.

--------------------------

data_Dict = {'Name': ['Subodh', 'Ram', 'Abdul', 'John'], 'Marks': [28, 27, 26, 28]}    ## --->>> Dictionary of 2 Lists
data_List = [{'Name': 'Subodh', 'Marks': 28},
        {'Name': 'Ram', 'Marks': 27},
        {'Name': 'Abdul', 'Marks': 26},
        {'Name': 'John', 'Marks': 28}]                                             ## --->>> List of 4 Dictionary
data_Dict_L=pd.DataFrame(data_Dict)
data_List_D=pd.DataFrame(data_List)
print(data_Dict_L)
print(data_List_D)

####### Output of Both is same #######

     Name  Marks
0  Subodh     28
1     Ram     27
2   Abdul     26
3    John     28

data_Dict_L1=data_Dict_L.set_index("Name")
print(data_Dict_L1[['Marks']])                                                                          #         Marks
                                                                                                        # Name
                                                                                                        # Subodh     28
                                                                                                        # Ram        27
                                                                                                        # Abdul      26
                                                                                                        # John       28

--------------------------
marks = {'Chemistry': [67,90,66,32],
        'Physics': [45,92,72,40],
        'Mathematics': [50,87,81,12],
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)

#######-------OUTPUT--------#######

        Chemistry  Physics  Mathematics  English
Subodh         67       45           50       19
Ram            90       92           87       90
Abdul          66       72           81       72
John           32       40           12       68


#------------------- Adding/Removing columns in a DataFrame ------------------

marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
print(marks_df)

#######-------OUTPUT--------#######

        Chemistry  Physics  Mathematics  English  Total
Subodh         67       45           50       19    181
Ram            90       92           87       90    359
Abdul          66       72           81       72    291
John           32       40           12       68    152


#------------------- To drop a feature: --------------------------

marks_df.drop(columns = 'Total', inplace = True)
print(marks_df)


        Chemistry  Physics  Mathematics  English
Subodh         67       45           50       19
Ram            90       92           87       90
Abdul          66       72           81       72
John           32       40           12       68


-------------------------------------------------------------

#######-------OUTPUT--------#######

########### Exploring the data ##########

1. Head and Tail : df.head()   and    df.tail()
-- To view the first few rows or the last few rows, the functions that can be used are: df.head() and df.tail() respectively.
-- If the number of rows to be viewed is not passed, then, the head and tail functions provides five rows by default.


2. Describe : df.describe()
-- The describe function can be used to generate a quick summary of data statistics.


3. Info : df.info()
-- To know about the datatypes and number of rows containing null values for respective columns, the info() function can be used.


4. Dropping null values : df.dropna(inplace = True)
-- It can be observed that the ‘horsepower’ attribute has some null values.
-- The easiest approach is to remove the rows with any null values. This can be achieved using dropna() function.

## Note:
-- 'inplace' makes changes to the original DataFrame.
-- df.fillna(condition) can be used to fill all the missing values. The missing values are filled with mean, median, mode, or constant values.


import pandas as pd
df = pd.read_csv('D:\\INFY COURSE\\PythonForDataScienceCodeData\\auto_mpg.csv')
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
df.dropna(inplace = True)
print(df.info())
print(df.columns[0:])     ----->>>>>>   Index(['mpg', 'cylinders', 'displacement', 'horsepower', 'weight','acceleration', 'model_year', 'origin', 'name'],dtype='object')


########### df.describe() #########

              mpg   cylinders  ...  acceleration  model_year
count  398.000000  398.000000  ...    398.000000  398.000000
mean    23.514573    5.454774  ...     15.568090   76.010050
std      7.815984    1.701004  ...      2.757689    3.697627
min      9.000000    3.000000  ...      8.000000   70.000000
25%     17.500000    4.000000  ...     13.825000   73.000000
50%     23.000000    4.000000  ...     15.500000   76.000000
75%     29.000000    8.000000  ...     17.175000   79.000000
max     46.600000    8.000000  ...     24.800000   82.000000

[8 rows x 7 columns]

########### df.info()  - before dropping null #########

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   mpg           398 non-null    float64
 1   cylinders     398 non-null    int64
 2   displacement  398 non-null    float64
 3   horsepower    392 non-null    float64
 4   weight        398 non-null    int64
 5   acceleration  398 non-null    float64
 6   model_year    398 non-null    int64
 7   origin        398 non-null    object
 8   name          398 non-null    object
dtypes: float64(4), int64(3), object(2)
memory usage: 28.1+ KB
None


########### df.info()  - after dropping null #########

<class 'pandas.core.frame.DataFrame'>
Int64Index: 392 entries, 0 to 397
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   mpg           392 non-null    float64
 1   cylinders     392 non-null    int64
 2   displacement  392 non-null    float64
 3   horsepower    392 non-null    float64
 4   weight        392 non-null    int64
 5   acceleration  392 non-null    float64
 6   model_year    392 non-null    int64
 7   origin        392 non-null    object
 8   name          392 non-null    object
dtypes: float64(4), int64(3), object(2)
memory usage: 30.6+ KB
None



######### Retrieve details of all the cars built in year 72. #########

print(df.loc[df['model_year'] == 72 ])


######### Retrieve details of all the cars built in Japan having 6 cylinders #########

print(df.loc[(df['origin'] == 'japan') & (df['cylinders'] == 6)])

--------------------------------------------------

print("##### Fuel Efficient ######\n")
print(df.loc[(df['mpg'] >29) & (df['horsepower'] < 93.5) & (df['weight'] < 2500)])
print("##### Muscle Cars ######\n")
print(df.loc[(df['displacement'] >262) & (df['horsepower'] > 126) & (df['weight'] > 2800) & (df['weight'] < 3600)])
print("##### SUV ######\n")
print(df.loc[(df['horsepower'] > 140) & (df['weight'] > 4500)])
print("##### RaceCar ######\n")
print(df.loc[(df['acceleration'] > 17) & (df['weight'] < 2223)])

--------------------------------------------------



########### Masking Operation ###########

-- The masking operation replaces values where the condition is True.

Syntax:  DataFrame.mask(cond, other = NaN, inplace = False, axis = None)

       cond    – Where cond is False, keep the original value. Where True, replace with corresponding value from other
       other   - Entries where cond is True are replaced with corresponding value from other.
       inplace - Whether to perform the operation in place on the data.
       axis    – alignment axis

## EXAMPLE - The marks of failed students has to be replaced with ‘Fail’    ##

marks = [{'Chemistry': 67, 'Physics': 45, 'Mathematics': 50, 'English' : 19},
        {'Chemistry': 90, 'Physics': 92, 'Mathematics': 87, 'English' : 90},
        {'Chemistry': 66, 'Physics': 72, 'Mathematics': 81, 'English' : 72},
        {'Chemistry': 32, 'Physics': 40, 'Mathematics': 12, 'English' : 68}]
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
f = marks_df < 33
print(marks_df.mask(f, 'Fail'))

###--- OUTPUT ---###

       Chemistry  Physics Mathematics English
Subodh        67       45          50    Fail
Ram           90       92          87      90
Abdul         66       72          81      72
John        Fail       40        Fail      68





############ Sorting Data ###########

print(df.sort_values(by = 'cylinders'))                                        # ------>>> The data sorted according to the number of cylinders.
print(df.sort_values(['cylinders'], ascending = 1))                            # ------>>> By default ascending=True

print(df.sort_values(['acceleration', 'horsepower'], ascending = (1,0)))       # ------>>> Data sorted in ascending order of acceleration and descending order of horsepower.



########### Preserving index ###########

-- Pandas preserves the index and column labels in the output.
-- For binary operations such as addition and multiplication, Pandas will automatically align indices when passing the objects to the functions.
-- In Below example -->> The  encrypted marks are with same indices as the original marks. This is called as index preservation.

marks = {'Chemistry': [67,90,66,32],
        'Physics': [45,92,72,40],
        'Mathematics': [50,87,81,12],
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)
encrypted_marks = np.sin(marks_df)
print(encrypted_marks)


##### OUTPUT ######

        Chemistry  Physics  Mathematics  English
Subodh         67       45           50       19
Ram            90       92           87       90
Abdul          66       72           81       72
John           32       40           12       68

        Chemistry   Physics  Mathematics   English
Subodh  -0.855520  0.850904    -0.262375  0.149877
Ram      0.893997 -0.779466    -0.821818  0.893997
Abdul   -0.026551  0.253823    -0.629888  0.253823
John     0.551427  0.745113    -0.536573 -0.897928


########### Resetting Index: ###########

-- In case of a requirement where the index has to be restored to the default index, reset_index() function must be used.
-- It adds the existing index as a new column in the DataFrame. This can be done as follows:

encrypted_marks.reset_index(inplace = True)
print(encrypted_marks)

##### OUTPUT ######

    index  Chemistry   Physics  Mathematics   English
0  Subodh  -0.855520  0.850904    -0.262375  0.149877
1     Ram   0.893997 -0.779466    -0.821818  0.893997
2   Abdul  -0.026551  0.253823    -0.629888  0.253823
3    John   0.551427  0.745113    -0.536573 -0.897928



########### Apply ###########

-- This method is used to apply a function along an axis of the DataFrame.
-- Syntax:
            DataFrame.apply(func, axis = 0, result_type = None)
                               func : Function to apply to each column or row.[ e.g., np.sum , np.mean ]
                               axis: Axis along which the function is applied.(0 --> along y axis for column sum , 1 --> along x axis for row sum)
                               result_type: one out of 'expand', 'reduce' or 'broadcast'. In the demo, 'broadcast' is used.
-- ‘broadcast’ : results will be broadcast to the original shape of the DataFrame, the original index and columns will be retained.

print(marks_df.apply(np.sum, axis = 1))
print(marks_df.apply(np.sum, axis = 1, result_type = "broadcast"))

##### OUTPUT ######

Subodh    181
Ram       359
Abdul     291
John      152
dtype: int64

        Chemistry  Physics  Mathematics  English
Subodh        181      181          181      181
Ram           359      359          359      359
Abdul         291      291          291      291
John          152      152          152      152



########### Aggregation operation in Pandas ###########


"""
import pandas as pd
import numpy as np
df = pd.DataFrame([[54.2,'a'],[658,'d']],
                  index = list('pq'))
df.columns = df.index
print(df.columns.values)

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
#
# df = pd.read_csv('D:\\INFY COURSE\\PythonForDataScienceCodeData\\auto_mpg.csv')
# df.dropna(inplace = True)
# X = df.iloc[:, 1:8]
# #Creating target
# y = df.iloc[:, 0]
# X = pd.get_dummies(X)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#
# scale = StandardScaler()
# scale.fit_transform(X_train)
# scale.transform(X_test);
#
# #Importing and fitting the model on training set
# reg = LinearRegression()
# #Fitting the model on training data :
# reg.fit(X_train, y_train)
# #Checking the coefficient(slope) and intercept.
# #'m' represents the coefficient and 'c' represents the intercept.
# m = reg.coef_
# c = reg.intercept_
# print(c,m)
#
# #Predicting the target: mpg against the predictors in the training data set
# #Predicted data stored in y_pred_train
# y_pred_train = reg.predict(X_train)
# #Predicting the target: mpg against the predictors in the testing data set
# #Predicted data stored in y_pred_test
# y_pred_test = reg.predict(X_test)
#
# # Prediction Accuracy in terms of how close is the predicted value of target: mpg
# # to the real value in training data set
# r2_S = r2_score(y_train, y_pred_train)
# print(r2_S)
#
# # Prediction Accuracy in terms of how close the predicted value of target: mpg
# # to the real value in testing data set
# from sklearn.metrics import r2_score
# r2_S = r2_score(y_test, y_pred_test)
# print(r2_S)
