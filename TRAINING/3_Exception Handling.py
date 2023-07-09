"""

An exception is an error that occurs during the execution of code.
This error causes the code to raise an exception and if not prepared to handle ,
it will halt the execution of the code.

--ZeroDivisionError   --- occurs when you try to divide by zero.
--NameError           --- occurs when we use the variable when it was not defined.
--IndexError          --- occurred when we tried to access data from a list using an index that
                          does not exist for this list.
etc -- https://docs.python.org/3/library/exceptions.html




############Exception Handling #########

-- Try Except --

A try except will allow you to execute code that might raise an exception and in the case of any exception
or a specific one we can handle or catch the exception and execute specific code.
This will allow us to continue the execution of our program even if there is an exception.

Python tries to execute the code in the try block.
In this case if there is any exception raised by the code in the try block, it will be caught
and the code block in the except block will be executed. After that, the code that comes after
the try except will be executed.


< potential code before try catch >
try:
    # code to try to execute
except:
    # code to execute if there is an exception
< code that will still execute if there is an exception >



-- Try Except Specific --

A specific try except allows you to catch certain exceptions and also execute certain code depending on the exception.
This is useful if you do not want to deal with some exceptions and the execution should halt.
It can also help you find errors in your code that you might not be aware of.
Furthermore, it can help you differentiate responses to different exceptions.
In this case, the code after the try except might not run depending on the error.

//1//

< potential code before try catch >
try:
    <# code to try to execute>
except (ZeroDivisionError, NameError):
    <# code to execute if there is an exception of the given types>
< code that will execute if there is no exception or a one that we are handling >

//2//

< potential code before try catch >
try:
    <# code to try to execute >
except ZeroDivisionError:
    <# code to execute if there is a ZeroDivisionError >
except NameError:
    <# code to execute if there is a NameError >
< code that will execute if there is no exception or a one that we are handling >



-- You can also have an empty except at the end to catch an unexpected exception:

< potential code before try catch >
try:
    <# code to try to execute >
except ZeroDivisionError:
    <# code to execute if there is a ZeroDivisionError >
except NameError:
    <# code to execute if there is a NameError >
except :
    <# code to execute if ther is any exception >
< code that will execute if there is no exception or a one that we are handling >


---------------------------------------------------------------------------
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
---------------------------------------------------------------------------



--- Try Except Else and Finally ---

-- else allows one to check if there was no exception when executing the try block.
This is useful when we want to execute something only if there were no errors.

-- finally allows us to always execute something even if there is an exception or not.
This is usually used to signify the end of the try except.


a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")


"""

try:
    print(10)

except:
    print("code to execute if there is an exception")