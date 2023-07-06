# Python Program to detect cycle in an undirected graph
from collections import defaultdict
# This class represents a undirected graph using adjacency list representation
class Graph:

	def __init__(self, vertices):

		self.V = vertices 										# No. of vertices
		self.graph = defaultdict(list)							# Default dictionary to store graph


	def addEdge(self, v, w):									# Function to add an edge to graph

		self.graph[v].append(w)									# Add w to v_s list
		self.graph[w].append(v)									# Add v to w_s list


	def isCyclicUtil(self, v, visited, parent):					# A recursive function that uses visited[] and parent to detect  cycle in subgraph reachable from vertex v.

		visited[v] = True										# Mark the current node as visited

		for i in self.graph[v]:									# Recur for all the vertices adjacent to this vertex

			if visited[i] == False:								# If the node is not visited then recurse on it
				if(self.isCyclicUtil(i, visited, v)):
					return True

			elif parent != i:									# If an adjacent vertex is visited and not parent of current vertex,then there is a cycle
				return True

		return False											# Returns true if the graph contains a cycle, else false.



	def isCyclic(self):

		visited = [False]*(self.V)								# Mark all the vertices as not visited

		for i in range(self.V):									# Call the recursive helper function to detect cycle in different DFS trees

			if visited[i] == False:								# Don't recur for u if it is already visited
				if(self.isCyclicUtil
				(i, visited, -1)) == True:
					return True

		return False

# Create a graph as per input File

sam_list=[]
inputFile = "inputPS10.txt"
outputFile = "outputPS10.txt"
with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        sam_list.append(x)
        sam_list.append(y)

result = [i for n, i in enumerate(sam_list) if i not in sam_list[:n]]
print(str(result))
List_len=len(result)
print(List_len)

g = Graph(List_len)

with open(inputFile, "r") as file1:
    for line in file1:
        x, y = line.split()
        g.addEdge(x, y)


print(g.graph)
if g.isCyclic():
	print("Graph contains cycle")
else:
	print("Graph doesn't contain cycle ")

