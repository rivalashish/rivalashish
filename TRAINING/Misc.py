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
f = open('inputPS10.txt', 'r')
T = []
E = 0  # no of edges
for line in f:
    E = E + 1
    T1 = line.split()
    (x, y) = T1
    T = T + T1
T = list(map(int, T))
N = set(T)
V = int(max(N))


class Graph:
    g = [[0 for x in range(V + 1)] for y in range(V + 1)]
    ci = []

    def __init__(self, n):
        self.n = n

    # def display(self):
    # for x in range(self.n):
    # for y in range(self.n):
    # print(" ",self.g[x][y],end=" ")
    # print()
    def addedge(self, x, y):
        self.g[x][y] = 1

    def OF(self, c1, c2, p, q):
        for i in range(self.n):
            if (Graph.g[i][c1] == 1 and i != c2) and (Graph.g[i][p] == 1 or Graph.g[i][q] == 1):
                # print(i,end=" ")
                Graph.ci.append(i)
                self.OF(i, c2, p, q)

    print(set(Graph.ci))

    def DFS(self, start, visited):
        # print(start, end = ' ')
        visited[start] = True
        for i in range(self.n):
            if (Graph.g[start][i] == 1 and (not visited[i])):
                self.DFS(i, visited)
            elif (Graph.g[start][i] == 1 and (visited[i])):
                # print(i,start,end=" ")
                Graph.ci.append(i)
                Graph.ci.append(start)
                p = i
                q = start
                self.OF(i, start, p, q)


ob = Graph(V + 1)
F = len(T)
for i in range(0, F, 2):
    (x, y) = (int(T[i]), int(T[i + 1]))
    ob.addedge(x, y)

# ob.display()
v = V + 1
visited = [False] * v
ob.DFS(1, visited);