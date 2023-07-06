inputFile = "inputPS10.txt"
outputFile = "outputPS10.txt"
Elements=[]
with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        Elements.append(x)
        Elements.append(y)
    MatrixSize=max(list(map(int,Elements)))



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

        # updating the adjacency matrix --> NxN matrix for row and column 0
        for source in range(0, self.n):
            for destination in range(0, self.n):
                self.g[source][destination] = 0

    def add_vertex(self, source, destination):
        # intialize source Index and destination index with 0
        index_s = 0
        index_d = 0
        # check if source vertex available in list  listofVertex, if not present then add it
        if source in self.liftoffVertex:
            index_s = self.liftoffVertex.index(source)
        else:
            print("Vertex {0} not present in Graph, adding now.".format(source))
            self.liftoffVertex.append(source)
            index_s = self.liftoffVertex.index(source)
            # addition of vertex done so increment the count of vertex
            self.n = self.n + 1

        # check if destination vertex available in list  listofVertex, if not present then add it
        if destination in self.liftoffVertex:
            index_d = self.liftoffVertex.index(destination)
        else:
            print("Vertex {0} not present in Graph, adding now.".format(destination))
            self.liftoffVertex.append(destination)
            index_d = self.liftoffVertex.index(destination)
            # addition of vertex done so increment the count of vertex
            self.n = self.n + 1

        if (index_s >= self.n) or (index_d >= self.n):
            print("One of the vertex doesn't exists !")

        if self.n > 1:
            for i in range(0, self.n):
                self.g[i][self.n - 1] = 0
                self.g[self.n - 1][i] = 0

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


MinValue=min(Elements)
g1 = GraphAM(MinValue)

with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        g1.add_vertex(x,y)
with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        g1.add_edge(x,y)

g1.print_graph()






Dict=g1.print_Friends_Circle()
print(Dict)
a=Dict.keys()
print(a)

for key in a:
    ele_list=Dict[key]
    Additional_ele=[]
    for ele in ele_list:
        if ele in Dict.keys():
            Additional_ele+=Dict[ele]

    Additional_ele.sort()
    temp=0
    Final_ele=[]

    for ele in  Additional_ele:
        if ele in ele_list:
            Final_ele.append(ele)

    for ele in  Additional_ele:
        if (temp == ele):
            Final_ele.append(ele)
        temp = ele
    if len(Final_ele)>0:
        ele_list+=Final_ele
        ele_set=set(ele_list)
        print ("Friends circle –",key,*ele_set, sep =' ')