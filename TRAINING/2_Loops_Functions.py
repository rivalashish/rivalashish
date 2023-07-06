"""
######################################## if-else ########################################
# Use if else statement and 'in' operator to compare the string

    if text in string:
        return 'String matched'
    else:
        return 'String not matched'



######################################## LOOPS ########################################

FOR LOOP ########################################

--  enables to execute a code block multiple times;
    can be used to print out every element in a list.
    the for loop is used for a controlled flow of repetition.

##1.##

dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])

//The code in the indent is executed N times, each time the value of i is increased by 1 for every execution.
//Output
1982
1980
1973

##2.##

squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

//Output
red
yellow
green
purple
blue

WHILE LOOP ########################################

-- While loop exists as a tool for repeated execution based on a condition.
   The code block will keep being executed until the given logical condition returns a False boolean value.

##1.##

dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")

//Output

1982
1980
It took  2 repetitions to get out of loop.

##2.##

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
while(i<len(PlayListRatings) and PlayListRatings[i]>=6):
    print(PlayListRatings[i])
    i+=1

//Output
10
9.5
10
8
7.5

##3.##

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(i<len(squares) and squares[i]=="orange"):
    new_squares.append(squares[i])
    i+=1
print(new_squares)

//Output
['orange', 'orange']



-------------------------------------------------------------------------------------------------------------


######################################## FUNCTIONS ########################################

A function is a reusable block of code which performs operations specified in the function.
They let you break down tasks and allow you to reuse your code in different programs.

-- There are two types of functions :
1. Pre-defined functions
2. User defined functions


## User defined functions ########################################

-- Rules to define a function in Python:

1.Function blocks begin def followed by the function name and parentheses ().
2.There are input parameters or arguments that should be placed within these parentheses.
3.You can also define parameters inside these parentheses.
4.There is a body within every function that starts with a colon (:) and is indented.
5.You can also place documentation before the body.
6.The statement return exits a function, optionally passing back a value.

-- The input to a function is called a formal parameter.
-- A variable that is declared inside a function is called a local variable.
   The parameter only exists within the function (i.e. the point where the function starts and stops).
-- A variable that is declared outside a function definition is a global variable,
   and its value is accessible and modifiable throughout the program.


#//1// Function example: Add 1 to a and store and return as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)
add(1)
--Output--
1 if you add one 2
2


#//2// Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
result = Mult(12,2)
print(result)
--Output--
24


#//3//  ##Use mult() multiply two different type values together##

Mult(2, "Michael Jackson ")
--Output--
Michael Jackson Michael Jackson


#//4// ## Python Program to Count words in a String using Dictionary ##

def freq(string):
    words = []                                           #step1: A list variable is declared and initialized to an empty list.
    words = string.split() # or string.lower().split()   #step2: Break the string into list of words
    Dict = {}                                            #step3: Declare a dictionary
    for key in words:                                    #step4: Use for loop to iterate words and values to the dictionary.
        Dict[key] = words.count(key)
    print("The Frequency of words is:",Dict)             #step5: Print the dictionary

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")      #step6: Call function and pass string in it

--OUTPUT--

The Frequency of words is: {'Mary': 6, 'had': 2, 'a': 2, 'little': 3, 'lamb': 3, 'Little': 1, 'lamb,': 1,
'lamb.Its': 1, 'fleece': 1, 'was': 2, 'white': 1, 'as': 1, 'snow': 1, 'And': 1, 'everywhere': 1, 'that': 2, 'went': 3,
 'went,': 1, 'Everywhere': 1, 'The': 1, 'sure': 1, 'to': 1, 'go': 1}


 #//5// ##

artist = "Michael Jackson"
def printer(artist):
    global internal_var                     // DECLARING GLOBAL VARIABLE FROM WITHIN A FUNCTION
    internal_var= "Whitney Houston"
    print(artist,"is an artist")
printer(artist)
printer(internal_var)

## Pre defined functions ########################################

1.print()
2.sum()
3.len()




## Functions and Collections :  ########################################

-- Functions can be incredibly powerful and versatile.
   They can accept (and return) data types, objects and even other functions as arguments
-- When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:

## //1// All the arguments are 'packed' into args which can be treated like a tuple


def printAll(*args):
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
printAll('Horsefeather','Adonis','Bone')                     #printAll with 3 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')      #printAll with 4 arguments

//OUTPUT//

No of arguments: 3
Horsefeather
Adonis
Bone
No of arguments: 4
Sidecar
Long Island
Mudslide
Carriage

## //2//  All the arguments are 'packed' into args which can be treated like a dictionary.
          // we are passing args in diff format but in args it will be taken same as dict.

def printDictionary(**args):
    print(args)
    for key in args:
        print(key + " : " + args[key])
printDictionary(Country='Canada',Province='Ontario',City='Toronto')

//OUTPUT//

{'Country': 'Canada', 'Province': 'Ontario', 'City': 'Toronto'}
Country : Canada
Province : Ontario
City : Toronto


## //3//

def addItems(list):
    list.append("Three")
    list.append("Four")
myList = ["One","Two"]
addItems(myList)
myList

//OUTPUT//

['One', 'Two', 'Three', 'Four']

--Note how the changes made to the list are not limited to the functions scope.
  This occurs as it is the lists reference that is passed to the function -
  Any changes made are on the original instance of the list.
  Therefore, one should be cautious when passing mutable objects into functions.




########### LAMBDA EXPRESSIONS ###########

-->> Lambda functions are one time use anonymous function , no name attached to it.
-->> map can be replaced with filter/reduce/zip


my_list=[1,2,3]
print (list(map(lambda item: item*2,my_list)))



"""
A=['hello', 'World']
for i in (enumerate(A)):
    print(A)

