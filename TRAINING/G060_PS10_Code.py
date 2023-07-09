inputFile = "inputPS10.txt"
outputFile = "outputPS10.txt"
with open(outputFile, "w") as Out_File:
    pass
Elements_List = []
Elements_Set = set()

try:
    with open(inputFile, "r") as file1:
        for line in file1:
            x, y = line.split()
            Elements_List.append(x)
            Elements_List.append(y)
            Elements_Set.add(int(x))
            Elements_Set.add(int(y))

    MatrixSize = max(list(map(int, Elements_List)))
    Serial_Num = 1
    temp_Neighbour = 0
    counter = 0
    Additional_List = []
    Final_List = []

    try:
        # Graph using adjacency matrix without importing any Libraries (without use of Dictionary)
        class GraphAM:
            # adjacency matrix of size n*n initialize with 0,n=MatrixSize
            g = [[0 for column in range(MatrixSize)] for row in range(MatrixSize)]
            listofVertex = []

            # Class Constructor
            def __init__(self, vertex):

                # adding a vertex in a list
                self.listofVertex.append(vertex)

                # saving no of vertices
                self.n = len(self.listofVertex)

                # Lists to prevent double entry of elements and avoid double entry of Friends circle in output File
                self.Additional_List = Additional_List
                self.Final_List = Final_List

                # updating the adjacency matrix --> NxN matrix for row and column with value --> 0
                for source in range(0, self.n):
                    for destination in range(0, self.n):
                        self.g[source][destination] = 0

            # Method to add Vertex
            def add_vertex(self, vertex):
                index_vertex = 0

                # check if source vertex available in list  listofVertex, if not present then add it
                if vertex in self.listofVertex:
                    index_vertex = self.listofVertex.index(vertex)
                else:
                    self.listofVertex.append(vertex)
                    index_vertex = self.listofVertex.index(vertex)
                    # addition of vertex done so increment the count of vertex
                    self.n = self.n + 1

                if index_vertex >= self.n:
                    print("One of the vertex doesn't exists !")

                # intialize values with 0 for all elements of Matrix
                if self.n > 1:
                    for i in range(0, self.n):
                        self.g[i][self.n - 1] = 0
                        self.g[self.n - 1][i] = 0

            # Method to add Edge
            def add_edge(self, source, destination):
                # initialize source Index and destination index with 0
                index_s = 0
                index_d = 0
                if source in self.listofVertex:
                    index_s = self.listofVertex.index(source)
                else:
                    print("Cannot be included in the graph ,  Add the vertex {0}".format(source))

                if destination in self.listofVertex:
                    index_d = self.listofVertex.index(destination)
                else:
                    print("Cannot be included in the graph ,  Add the vertex {0}".format(destination))

                if index_s > 0 and index_s == index_d:
                    print("Same Source and Destination")
                else:
                    # Adding edge considering source is smaller in value than destination vertex
                    if index_s < index_d:
                        self.g[index_s][index_d] = 1
                    else:
                        self.g[index_d][index_s] = 1

            # To get the list of friends in forward direction
            def get_Friends_List(self, Friend):
                Ele_List = []
                for count in range(0, MatrixSize):
                    if self.g[int(Friend) - 1][count] == 1:
                        Ele_List.append(str(count + 1))
                return Ele_List

            # To get the list of friends in backward direction
            def get_Reverse_Friends_List(self, Friend):
                Ele_List = []
                for count in range(0, MatrixSize):
                    if self.g[count][int(Friend) - 1] == 1:
                        Ele_List.append(str(count + 1))
                return Ele_List

            # To backtrack the friends - Part of DFS
            def DFS_BackTracking(self, neighbour, v, c, visited):
                global counter
                global temp_Neighbour
                for vertex in self.listofVertex:
                    if vertex in visited and neighbour != temp_Neighbour:
                        k = vertex
                        Ele_List1 = self.get_Friends_List(k)
                        for i in Ele_List1:
                            if i == neighbour and (k not in Additional_List or (counter > 0 and counter % 2 != 0)):

                                self.Final_List.append(int(k))
                                neighbour = k
                                counter += 1
                                self.Additional_List.append(k)
                                self.Additional_List.append(v)
                                if counter > 0 and counter % 2 == 0:
                                    temp_Neighbour = k
                                    self.DFS_BackTracking(c, v, c, visited)
                                self.DFS_BackTracking(neighbour, v, c, visited)

            # To track the friends in forward direction - Part of DFS
            def DFSUtil(self, v, visited):
                global Serial_Num
                global counter
                visited.add(v)
                # print("\n",v,end=" ")
                Ele_List2 = self.get_Friends_List(v)

                for neighbour in Ele_List2:
                    counter = 0
                    self.Final_List = []
                    neighbour_List = self.get_Reverse_Friends_List(neighbour)
                    for neighbour_friend in neighbour_List:
                        if neighbour_friend not in visited:
                            self.DFSUtil(neighbour_friend, visited)
                            self.Final_List = []
                            counter = 0

                    if neighbour not in visited:
                        self.DFSUtil(neighbour, visited)
                    else:

                        Additional_List = []

                        self.Final_List.append(int(neighbour))
                        self.Final_List.append(int(v))
                        self.Additional_List.append(neighbour)
                        self.Additional_List.append(v)

                        c = neighbour
                        self.DFS_BackTracking(neighbour, v, c, visited)
                        with open(outputFile, "a+") as Out_File:
                            if len(self.Final_List) > 3 and self.Final_List not in Out_File:
                                Final_Set = set(self.Final_List)
                                self.Final_List = (list(Final_Set))
                                print(Serial_Num, ". Friends circle –", *self.Final_List, sep=' ', file=Out_File)
                                Serial_Num = Serial_Num + 1
            # DFS Method
            def DFS(self):
                visited = set()
                for vertex in self.listofVertex:
                    if vertex not in visited:
                        self.DFSUtil(vertex, visited)

    except:
        print("Something went wrong --->>> Check Class Definition")

    try:
        MinValue = min(Elements_List)
        g = GraphAM(MinValue)

        for ele in Elements_Set:
            g.add_vertex(str(ele))

        with open(inputFile, "r") as file1:
            for line in file1:
                x, y = line.split()
                g.add_edge(x, y)
        g.DFS()
    except:
        print("Something went wrong -->>> Check 3rd try Block")


except ValueError:
    print("You did not provide a expected number input ---> e.g., 1 2")
except FileNotFoundError:
    print("Please Check the Input File ,if Exists ?")
except:
    print("Something went wrong -->>> Check 3rd try Block")
