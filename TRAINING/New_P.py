f = open('inputPS10.txt', 'r')
T = []
E = 0  # no of edges
for line in f:
    E = E + 1
    T1 = line.split()
    #(x, y) = T1
    T = T + T1
T = list(map(int, T))
#V = int(max(set(T)))
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def Otherfriend(self, neighbour, v, c):
        for vertex in list(self.graph):
            k = vertex
            for i in self.graph[k]:
                if i == neighbour:
                    print(k, end=" ")
                    neighbour = k
                    self.Otherfriend(neighbour, v, c)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print("\n",v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
            else:
                print("\ncircle is", end=" ")
                print(neighbour, v, end=" ")
                c = neighbour
                self.graph.pop(v)
                self.Otherfriend(neighbour, v, c)

    def DFS(self):
        visited = set()
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex, visited)


g = Graph()
F = len(T)
for i in range(0, F, 2):
    (x, y) = (int(T[i]), int(T[i + 1]))
    g.addEdge(x, y)
g.DFS()





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
