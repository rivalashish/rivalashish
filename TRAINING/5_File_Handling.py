"""

## Uncomment these if working locally, else let the following code cell run.

import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Download Example file
!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt



from pyodide.http import pyfetch
import pandas as pd
import skillsnetwork
await skillsnetwork.download_dataset("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt")
df = open("example1.txt")




#############################  Opening / Reading Text Files  ############################

######## Open Function ########

-- To read or write a file in Python - the built-in open function
-- The open function provides a File object that contains the methods and attributes you need in order to read,
   save, and manipulate the file.

-- The mode argument is optional and the default value is r. In this notebook we only cover two modes:
     **r**: Read mode for reading files
     **w**: Write mode for writing files

# Read the Example1.txt
example1 = "D:\\Programs\\Python\\File_Handing_Sample.txt"
file1 = open(example1, "r")


# Print the path of file
print(file1.name)


# Print the mode of file, either 'r' or 'w'
print(file1.mode)


# Read the file
FileContent = file1.read()
FileContent


# Print the file with '\n' as a new line
print(FileContent)


# Type of file content
type(FileContent)


# Close file after finish
file1.close()



######## with Open Function ########

Using the with statement is better practice, it automatically closes the file even if the code encounters an exception.
The code will run everything in the indent block then close the file object.

# Open file using with:
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)



########### Read certain amount of characters (irrespective of new line or same line it will read)

with open(example1, "r") as file1:
    print(file1.read(4))             #// Read from character 1 to 4
    print(file1.read(4))             #// Read from character 5 to 8   i.e., next 4
    print(file1.read(7))             # // Read from character 9 to 15  i.e., next 7
    print(file1.read(15))            # // Read from character 16 to 30 i.e., next 15


############ Read one line  - readline()

with open(example1, "r") as file1:
    print("first line: " + file1.readline())    #// can also paas number of character to read.


# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1


############ Read all lines  - readlines() - We can use the method readlines() to save the text file to a list:

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()


# Print the first,second and third line
FileasList[0]
FileasList[1]
FileasList[2]





#############################  Writing Text Files  ############################

We can open a file object using the method write() to save the text file to a list.
To write to a file, the mode argument must be set to w.
Let’s write a file Example2.txt with the line: “This is line A”


# Write line to file
exmp2 = "D:\\Programs\\Python\\File_Handing_Sample1.txt"
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")


# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")


The method .write() works similar to the method .readline(),
except instead of reading a new line it writes a new line.


#### Write the strings in the list to text file as follows:

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

--  Note that setting the mode to w overwrites all the existing data in the file.





#############################  Appending Text Files  ############################

We can write to files without losing any of the existing data as follows by setting the mode argument to append: a.
you can append a new line as follows:

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")




############################ Additional modes ############################

It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines.

r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
a+ : Appending and Reading. Creates a new file, if none exists.
     You don't have to dwell on the specifics of each mode for this lab.


with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

# There were no errors but read() also did not output anything. This is because of our location in the file.


### Most of the file methods we've looked at work in a certain location in the file.
--  .write()  writes at a certain location in the file.
--  .read() reads at a certain location in the file and so on.

You can think of this as moving your pointer around in the notepad to make changes at specific location.


### Opening the file in
-- w is akin to opening the .txt file, moving your cursor to the beginning of the text file,
   writing new text and deleting everything that follows.
-- a is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text.

It is often very useful to know where the 'cursor' is in a file and be able to control it.

The following methods allow us to do precisely this -
-- .tell() - returns the current position in bytes
-- .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'.
                        From can take the value of 0,1,2 corresponding to beginning, relative to current position and end


with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):                                          #empty strings return false in python
            print('Read nothing')
    else:
            print(testwritefile.read())

    testwritefile.seek(0,0)                                 # move 0 bytes from beginning.
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
            print('Read nothing')
    else:
            print(data)

    print("Location after read: {}".format(testwritefile.tell()) )



Finally, a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however,
 -- opening a file in :
                  w+        --  overwrites it and deletes all pre-existing data.
                  r+ and a+ --  To work with a file on existing data.
    While using r+, it can be useful to add  .truncate() method at the end of your data.
    This will reduce the file to your data and delete everything that follows.

In the following code block, Run the code as it is first and then run it with the .truncate().


with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0)             #write at beginning of file

    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()          # This will remove everything that was part of file before writing anything to it.
    testwritefile.seek(0,0)
    print(testwritefile.read())


############################ Copy a File ############################

Let's copy the file Example2.txt to the file Example3.txt:

# Copy file to another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


-- After reading files, we can also write data into files and
   save them in different file formats like .txt, .csv, .xls (for excel files) etc.


"""

#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members

    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''


def cleanFiles(currentMem, exMem):
    List=[]
    # TODO: Open the currentMem file as in r+ mode
    # TODO: Open the exMem file in a+ mode
    # TODO: Read each member in the currentMem (1 member per row) file into a list.
    # Hint: Recall that the first line in the file is the header.
    # TODO: iterate through the members and create a new list of the innactive members
    # Go to the beginning of the currentMem file
    # TODO: Iterate through the members list.
    # If a member is inactive, add them to exMem, otherwise write them into currentMem
    with open(currentMem,'r+') as readFile_Curr:
        readFile_Curr.readline()
        while (readFile_Curr.readline()):
            a=readFile_Curr.readline()
            if(a.__contains__(" no ")):
                with open(exMem, 'a+') as appendFile_Ex:
                    appendFile_Ex.write(a)
            else:
                List.append(a)
    with open(currentMem, 'w+') as writeFile_Curr:
        with open(exMem, 'r+') as appendFile_Ex1:
            writeFile_Curr.write(appendFile_Ex1.readline())
        for line in List:
            line=str(line)
            writeFile_Curr.write(line)







# Remove this line when done implementation


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

