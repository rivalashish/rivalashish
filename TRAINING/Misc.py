"""
###### Single underscores ######

1.  A single leading underscore in front of a variable, a function,
or a method name means that these objects are used internally.
    This is more of a syntax hint to the programmer and is not enforced by the Python interpreter ,
which means that these objects can still be accessed in one way on another from another script.
    However, there’s a situation where a variable that has a leading underscore cannot be accessed directly,
possible if module is imported and then variable is called..--Private Variable


2.  A Single trailing underscores : There are some situations where you want to use a variable name that is actually
a reserved keyword in Python such as class, def , type , object , etc.
    To avoid this conflict, you can add a trailing underscore as a naming convention.

3.  A Single underscores : To define temporary or unused variables.

###### Double underscores ######

1.  Double leading and trailing underscores are used to define special universal class methods called
dunder methods (short for Double Underscore methods).
    Dunder methods are reserved methods that you can still overwrite.
They have special behavior and are called differently. For example:
    __init__ is used as a constructor of the class
    __call__ is used to make the object callable
    __str__ is used to define what’s printed on the screen when we pass the object to the print function.
As you see, Python introduces this naming convention to differentiate between the module’s core methods and
the user-defined ones.


 """
#
# # Python3 program to print DFS traversal
# # from a given given graph
# from collections import defaultdict
#
# # This class represents a directed graph using
# # adjacency list representation
#
#
# class Graph:
#
#     # Constructor
#     def __init__(self):
#
#         # default dictionary to store graph
#         self.graph = defaultdict(list)
#
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     # A function used by DFS
#     def DFSUtil(self, v, visited):
#
#         # Mark the current node as visited
#         # and print it
#         visited.add(v)
#         print(v, end=' ')
#
#         # Recur for all the vertices
#         # adjacent to this vertex
#         for neighbour in self.graph[v]:
#             if neighbour not in visited:
#                 self.DFSUtil(neighbour, visited)
#
#     # The function to do DFS traversal. It uses
#     # recursive DFSUtil()
#     def DFS(self, v):
#
#         # Create a set to store visited vertices
#         visited = set()
#
#         # Call the recursive helper function
#         # to print DFS traversal
#         self.DFSUtil(v, visited)
#
# # Driver code
#
#
# # Create a graph given
# # in the above diagram
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
#
# print("Following is DFS from (starting from vertex 2)")
# g.DFS(2)
#







# Python3 program to print DFS traversal
# from a given  graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        # print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
        return visited
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function
        # to print DFS traversal
        a=self.DFSUtil(v, visited)
        return a



# Driver's code


g = Graph()
List=[]
inputFile = "inputPS10.txt"
outputFile = "outputPS10.txt"
with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        g.addEdge(x, y)
        if x not in List:
            List.append(x)


# Function call
print(g.graph)
print(List)

Dict ={}

with open(outputFile, 'w') as writefile:
    for ele in List:
        out=g.DFS(ele)
        Dict[ele] =out

print(Dict)
# Intersection_Set=Dict[List[0]]
# for i in range (0,len(List)):
#     Values=Dict[List[i]]
#     for num in Values:
#         if num in Dict.keys():
#             Verteex=Dict[num]
#             Intersection_Set = Intersection_Set.intersection(Verteex)
#             print (Intersection_Set)