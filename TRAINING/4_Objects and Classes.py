"""
################### Creating a Class ######################

-- The first step in creating a class is giving it a name.
-- Their attributes, which are variables.
-- e.g.,Classes circle and rectangle, and each has their own attributes.
        The class Circle has the attribute radius and colour, the class Rectangle has the attributes height and width.


################### Instances of a Class: Objects and Attributes ###################

-- INSTANTIATION : Creating instances of a Class.

-- An instance of an object is the realisation of a class,We give each object a name.
-- Each object has different attributes

-- e.g., Classes circle and rectangle, and each has their own attributes.
   The class Circle has the attribute radius and colour, the class Rectangle has the attributes height and width.

-- The colour attribute for the red Circle is the colour red,
   for the green Circle object the colour attribute is green,
   and for the yellow Circle the colour attribute is yellow.



################### Methods ###################

-- Methods give you a way to change or interact with the object; they are functions that interact with objects.


import matplotlib
# Import the library
import matplotlib.pyplot as plt
from jedi.api.refactoring import inline


# Create a class Circle #

class Circle(object):                                                               ## Using class keyword

    # Constructor --                                          ## a special method called a constructor __init__, which is used to initialize the object ##
    def __init__(self, radius=3, color='blue'):               ## The inputs are data attributes. The term self contains all the attributes in the set.  ##
        self.radius = radius                                  ## To access the radius we use the syntax self. radius
        self.color = color

    # Method
    def add_radius(self, r):                                  ## method add_radius() with the parameter r, the method adds the value of r to the attribute radius.
        self.radius = self.radius + r
        return(self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()




###################################### Creating an instance of a class Circle ######################################


# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Print the object attribute radius
print(RedCircle.radius)
print(RedCircle.color)

# Set the object attribute radius
RedCircle.radius = 1
print(RedCircle.radius)

# Call the method drawCircle/add_radius
RedCircle.drawCircle()
RedCircle.add_radius(2)
print(RedCircle.radius)



------------------------------------------------------------------



class PlayerCharacter:
    membership=True                             # Class Object Attribute
    def __init__(self,name="",age=0):               ## Constructor for the class
        if (age>=18 and name!=""):
            self.name=name                          # Attributes and self refers to Class Player Character
            self.age=age

    @classmethod  ## class methods
    def cls_method(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod  ## static methods -- No direct access to class , so cannot use cls as in @classmethod
    def stc_method(param1, param2):
        return param1 + param2

    def run(self):                                  ## instance methods
        print(f"run -->> {self.name}")
        print(f'my name is {self.name} and age {self.age}')
        return "done"

player1=PlayerCharacter("Ashish",26)
player2=PlayerCharacter("Hardik",21)
player3=PlayerCharacter()
player2.attack=50
help(player1)

print(player1.run())
print(player2.age)
print(player2.attack)         # print(player1.attack) won't work
print(player1.membership)
print(player2.membership)
#print(player3.run())         # This is not working as no instantiation for player 3 , so self wont work as age and name by default is diff


player4=PlayerCharacter.cls_method(22,3)
print(player4.run())

print(PlayerCharacter.stc_method(2,3))

https://www.makeuseof.com/tag/python-instance-static-class-methods/

--------------------------------------------------------------------------------------
"""
import sys
#
#
# class analysedText(object):
#
#     def __init__(self, text):
#         text = text.lower()
#         text = text.replace(".", "")  # TODO: Remove the punctuation from <text> and make it lower case.
#         text = text.replace("!", "")  # TODO: Assign the formatted text to a new attribute called "fmtText"
#         text = text.replace(",", "")
#         self.fmtText = text.replace("?", "")
#
#     def freqAll(self):
#         Words_List = []  # TODO: Split the text into a list of words
#         Words_List = self.fmtText.split()  # TODO: Create a dictionary with the unique words in the text as keys and the number of times they occur in the text as values
#         Dict = {}  # return the created dictionary
#         for key in Words_List:
#             Dict[key] = Words_List.count(key)
#         return Dict
#
#     def freqOf(self, word):
#         Words_List = []  # TODO: return the number of occurrences of <word> in <fmtText>
#         Words_List = self.fmtText.split()
#         return Words_List.count(word)
#
#
# sampleMap = {'eirmod': 1, 'sed': 1, 'amet': 2, 'diam': 5, 'consetetur': 1, 'labore': 1, 'tempor': 1, 'dolor': 1,
#              'magna': 2, 'et': 3, 'nonumy': 1, 'ipsum': 1, 'lorem': 2}
#
#
# def testMsg(passed):
#     if passed:
#         return 'Test Passed'
#     else:
#         return 'Test Failed'
#
#
# print("Constructor: ")
# try:
#     samplePassage = analysedText(
#         "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
#     print(testMsg(
#         samplePassage.fmtText == "lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet"))
# except:
#     print("Error detected. Recheck your function ")
# print("freqAll: ")
# try:
#     wordMap = samplePassage.freqAll()
#     print(testMsg(wordMap == sampleMap))
# except:
#     print("Error detected. Recheck your function ")
# print("freqOf: ")
# try:
#     passed = True
#     for word in sampleMap:
#         if samplePassage.freqOf(word) != sampleMap[word]:
#             passed = False
#             break
#     print(testMsg(passed))
#
# except:
#     print("Error detected. Recheck your function  ")


class PlayerCharacter:
    membership=True                             # Class Object Attribute
    def __init__(self,name="",age=0):               ## Constructor for the class
        if (age>=18 and name!=""):
            self.name=name                          # Attributes and self refers to Class Player Character
            self.age=age

    @classmethod  ## class methods
    def cls_method(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod  ## static methods -- No direct access to class , so cannot use cls as in @classmethod
    def stc_method(param1, param2):
        return param1 + param2

    def run(self):                                  ## instance methods
        print(f"run -->> {self.name}")
        print(f'my name is {self.name} and age {self.age}')
        return "done"





player1=PlayerCharacter("Ashish",26)
player2=PlayerCharacter("Hardik",21)
player3=PlayerCharacter()
player2.attack=50
help(player1)

print(player1.run())
print(player2.age)
print(player2.attack)         # print(player1.attack) won't work
print(player1.membership)
print(player2.membership)
#print(player3.run())         # This is not working as no instantiation for player 3 , so self wont work as age and name by default is diff


player4=PlayerCharacter.cls_method(22,3)
print(player4.run())

print(PlayerCharacter.stc_method(2,3))