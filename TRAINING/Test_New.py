inputFile = "inputPS10.txt"
outputFile = "outputPS10.txt"
Elements_List=[]
Elements_Set=set()
with open(inputFile, "r") as file1:
    for line in file1:
        x, y= line.split()
        Elements_List.append(x)
        Elements_List.append(y)
        Elements_Set.add(int(x))
        Elements_Set.add(int(y))
    MatrixSize=max(list(map(int,Elements_List)))

# Graph using adjacency matrix
class GraphAM():
    # adjacency matrix of size 10x10 initialize with 0
    g = [[0 for column in range(MatrixSize)] for row in range(MatrixSize)]
    liftoffVertex = []

    def __init__(self, vertex):
        # adding a vertex in a list
        self.liftoffVertex.append(vertex)
        # saving no of vertices
        self.n = len(self.liftoffVertex)

        # updating the adjacency matrix --> NxN matrix for row and column with value --> 0
        for source in range(0, self.n):
            for destination in range(0, self.n):
                self.g[source][destination] = 0

    def add_vertex(self, vertex):
        # intialize source Index and destination index with 0
        index_vertex = 0
        # check if source vertex available in list  listofVertex, if not present then add it
        if vertex in self.liftoffVertex:
            index_vertex = self.liftoffVertex.index(vertex)
        else:
            print("Vertex {0} not present in Graph, adding now.".format(vertex))
            self.liftoffVertex.append(vertex)
            index_vertex = self.liftoffVertex.index(vertex)
            # addition of vertex done so increment the count of vertex
            self.n = self.n + 1

        if index_vertex >= self.n:
            print("One of the vertex doesn't exists !")

        if self.n > 1:
            for i in range(0, self.n):
                self.g[i][self.n-1] = 0
                self.g[self.n-1][i] = 0

    def add_edge(self, source, destination):
        # initialize source Index and destination index with 0
        index_s = 0
        index_d = 0
        if source in self.liftoffVertex:
            index_s = self.liftoffVertex.index(source)
        else:
            print("Cannot be included in the graph ,  Add the vertex {0}".format(source))

        if destination in self.liftoffVertex:
            index_d = self.liftoffVertex.index(destination)
        else:
            print("Cannot be included in the graph ,  Add the vertex {0}".format(destination))

        if index_s > 0 and index_s == index_d:
            print("Same Source and Destination")
        else:
            self.g[index_s][index_d] = 1
            #self.g[index_d][index_s] = 1



    def print_graph(self):
        print("\n")
        for i in range(len(self.liftoffVertex)):
            print("\t\t", self.liftoffVertex[i], end="")
        for i in range(0, self.n):
            print("\n", self.liftoffVertex[i], end="  ")
            for j in range(0, self.n):
                print("\t", self.g[i][j], end="   ")

        print("\n")

    def print_Friends_Circle(self):
        print("\n")
        Dict={}
        for i in range(0, self.n):
            friends_List=[]
            for j in range(0, self.n):
                if (self.g[i][j]==1):
                    friends_List.append(self.liftoffVertex[j])
            if (len(friends_List)>=1):
                key=self.liftoffVertex[i]
                Dict[key]=friends_List
                print("Friends circle –", self.liftoffVertex[i], *friends_List, sep =' ')
        return Dict

    def Otherfriend(self, neighbour, v, c):
        for vertex in self.liftoffVertex:
            vertex = int(vertex)
            k = vertex

            Ele_List1 = []
            for count in range(0, MatrixSize):
                print(k,count)
                if self.g[k - 1][count] == 1:
                    Ele_List1.append(count + 1)

            for i in Ele_List1:
                if i == neighbour:
                    print(k, end=" ")
                    neighbour = k
                    self.Otherfriend(neighbour, v, c)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v,end=" ")
        Ele_List2=[]
        for count in range (0,MatrixSize):
            if self.g[v - 1][count] == 1:
                Ele_List2.append(count+1)

        for neighbour in Ele_List2:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
            else:
                print("circle is", end=" ")
                print(neighbour, v, end=" ")
                c = neighbour
                self.g.pop(v)
                self.Otherfriend(neighbour, v, c)

    def DFS(self):
        visited = set()
        for vertex in self.liftoffVertex:
            if vertex not in visited:
                vertex=int(vertex)
                self.DFSUtil(vertex, visited)


MinValue=min(Elements_List)
g = GraphAM(MinValue)

print(Elements_Set)
for ele in Elements_Set:
    g.add_vertex(str(ele))

with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        g.add_edge(x,y)
g.print_graph()
g.DFS()