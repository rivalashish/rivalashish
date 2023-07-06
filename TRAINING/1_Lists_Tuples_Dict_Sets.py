"""

A-65 ; Z-90  ; a-97 ; z-122

######## TUPLE -- an ordered sequence,expressed as comma separated elements within parentheses ########
-- Immutable : Cant be changed.As below Tuple and Tuple1 both points to same set of values , thus if we change Tuple ,
                Tuple1 will also get changed. So if we want to update Tuple then better to redeclare that with desired one.
    Tuple=("abc",32,21)
    Tuple1=Tuple
    WRONG - Tuple[0]="xyz"
    CORRECT - Tuple=("xyz",32,21)

-- Nesting : Can store another tuple.
    Rating=(("abc",32),21,("xyz",38),25)

    Rating[0]=("abc",32)
    Rating[0][1]=32
    Rating[-1]=25

-- Concatenation :
    Tuple2=Tuple+("hard rock",22)  ; len(Tuple)=3    ==>> Tuple2=("abc",32,21,"hard rock",22) ; len(Tuple2)=5


-- Slicing :
    Tuple2[3:5]=("hard rock",22)

# Sort the tuple

Ratings=(2,5,99,62,32,31)
RatingsSorted = sorted(Ratings)   // This function does not change Ratings
RatingsSorted  -->> (2,55,31,32,62,99)

But ,if Ratings is a List (mutable) then ,
Ratings.sort() // Changes order of elements in Ratings , Ratings -->> [2,55,31,32,62,99]


##
Tuple2.index("hard rock")  --->>> 3

"""

# -------------------------------------------------------------------------------------------------------------------- #


"""

######## LISTS -- an ordered sequence ,represented with square brackets ########
-- Mutable : Can be changed.
        
        List=[110,2,10.5,"abcd"]
        List[0]=1
        List=[1,2,10.5,"abcd"] 
        
     Also , mutable thus can be extended/appended too.
     List=[1,2,10.5,"abcd"]                 ---- len(List)=4  
     
     List.extend(["pop",10])                ----  will append as two new elements.
     List=[1,2,10.5,"abcd","pop",10]        ---- len(List)=6   
     
     List.append(["pop",10])                ----  will append as one new element  .
     List=[1,2,10.5,"abcd",["pop",10[]      ---- len(List)=5 
    
-- Deletion :
    List=[1,2,10.5,"abcd"]
    del(List[2])
    List=[1,2,"abcd"]
    
-- Split :

    The method split separates a string into a list based on the argument.
    If there is no argument as in this case the string is split using spaces.

    "Hard Rock".split() =["Hard","Rock"]
    "A,B,C,D".split(",")=["A"."B","C","D"]    -- Here comma is used as delimiter
    
-- Nesting : Can store another tuple/list as well.
    List1=[10,28,11.5,["def",13],("xyz",39)]
    
-- Slicing :
    List1[3:5]=[["def",13],("xyz",39)]
    
-- Concatenation :
    List2=List+["hard rock",22]  ; len(List)=4    ==>> List2=["abc",32,21,"hard rock",22] ; len(List2)=6
    
-- Aliasing :
    A=["a","b","d",12]
    B=A  -- now both A and B are referring to same list so if we change A ,B will change as well.
    if A[0]="z"
    Thus , B[0] -- "z"
    
-- Cloning :
    A=["a","b","d",12]
    B=A[:]  -- now both A and B are referring to diff list so if we change A ,B will not change.
    if A[0]="z"
    Thus , B[0] -- "a"
    
   
    


"""


# ------------------------------------------------------------#
"""######## DICTIONARY -consists of keys and values.Instead of being indexed numerically like a list, dictionaries 
                        have keys. These keys are the keys that are used to access values within a dictionary.   ########
    -- Keys can be strings and can also be any immutable object such as a tuple.
    -- Keys can only be strings, numbers, or tuples, but values can be any data type.
    
    Empty Dictionary - {}
    Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

   # Get value by key
    Dict['key1'] -->> 1
    
   # Get all the keys in dictionary
    Dict.keys()
    
   # Get all the values in dictionary
    Dict.values()    
    
   # Append value with key into dictionary
    Dict['key1'] = 33
    
    # Delete the entry with key into dictionary
    del(Dict['key1'])
    
    # Verify the key is in the dictionary
    '2' in Dict
    

########### List of Dictionary ###########     
  
    -- A list of dictionaries means, the dictionary is present as an element in the list.  
    
    --  [{‘key’:element1,’key’:element2,……, ‘key’:element n}]
    --  data[index][key]
    
    where index is the dictionary index and the key is the dictionary key-value
    
# create a list of dictionary with student
# id as key and name as value
data = [{7058: 'sravan', 7059: 'jyothika', 7072: 'harsha', 7075: 'deepika'}]
 
# display data of key 7058
print(data[0][7058])
 
# display data of key 7059
print(data[0][7059])
 
# display data of key 7072
print(data[0][7072])
 
# display data of key 7075
print(data[0][7075])



########### List of multiple dictionaries ###########

    -- This is similar to the above approach, except that multiple dictionaries are being passed to the list at once.
    
# create a list of dictionaries with
# student id as key and name as value
data = [{7058: 'sravan', 7059: 'jyothika',
         7072: 'harsha', 7075: 'deepika'},
         
        {7051: 'fathima', 7089: 'mounika',
         7012: 'thanmai', 7115: 'vasavi'},
         
        {9001: 'ojaswi', 1289: 'daksha',
         7045: 'parvathi', 9815: 'bhavani'}]
 
# access third dictionary with key 9001
print(data[2][9001])
 
# access second dictionary with key 7012
print(data[1][7012])
 
# access second dictionary with key 7115
print(data[1][7115])



--------- Output:

ojaswi
thanmai
vasavi
    
"""

# ------------------------------------------------------------#
"""
######## SETS -- A set is a unique collection of objects in Python,denote a set with a pair of curly brackets {}. 
                        It will automatically remove duplicate items:########

    set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
    
    set1 -->> {"pop", "rock", "soul", "hard rock", "R&B",, "disco"}  // duplicates removed.
    
    # Add element to set
     A = set(["Thriller", "Back in Black", "AC/DC"])
     A.add("NSYNC")

    # Remove the element from set
     A.remove("NSYNC")
    
    # Verify if the element is in the set
     "AC/DC" in A
     
-- Sets Logic Operations: with sets ,can check the difference between sets, as well as the symmetric difference,
                            intersection, and union:
                            
    album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
    album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
    
    # Find the intersections
     intersection = album_set1 & album_set2         OR          album_set1.intersection(album_set2) 
     intersection -->> {'AC/DC', 'Back in Black'}
     
    # Find the difference in set1 but not set2:
      album_set1.difference(album_set2)  -->> {"Thriller"}
      
    -->> all the elements in album_set2, including the intersection are not included.
    -->> if set1 is after diff and set2 before then all the elements in album_set1, including the intersection are not included.

    # Find the union of two sets
     album_set1.union(album_set2)  -->> {'AC/DC', 'Back in Black',"Thriller","The Dark Side of the Moon"}
     
     
     
-- if a set is a superset or subset of another set, respectively, like this:

    set(album_set1).issuperset(album_set2)
    set(album_set2).issubset(album_set1)  
    
    
    set({"Back in Black", "AC/DC"}).issubset(album_set1)  -->> TRUE
    set({"Back in Black", "AC/DC"}).issubset(album_set1)  -->> TRUE
    

-- LIST TO SET:

        list -->> ['rap','house','electronic music', 'rap']
        set  -->> set(['rap','house','electronic music','rap'])
    
    
-- SUM :

A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])   -->> B={1,2}
print("the sum of A is:", sum(A))  -->> 6
print("the sum of B is:", sum(B))  -->> 3


    
"""
def freq(string):
    words = []                                           #step1: A list variable is declared and initialized to an empty list.
    words = string.split() # or string.lower().split()   #step2: Break the string into list of words
    Dict = {}                                            #step3: Declare a dictionary
    word_set=set(words)
    for key in word_set:                                    #step4: Use for loop to iterate words and values to the dictionary.
        Dict[key] = words.count(key)
    print("The Frequency of words is:",Dict)             #step5: Print the dictionary

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")      #step6: Call function and pass string in it