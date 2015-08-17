"""Data Structures
Working with Graphs/Networks"""

# Note that edges can have values
def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
#   if node2 not in G:
#     G[node2] = {}
#   (G[node2])[node1] = 1
  return G 

emptylist={}
makeLink(emptylist,1,1)  # This will create a new dictionary like this: {1: {1: 1}}

emptylist={}
makeLink(emptylist,2,1)

emptylist={}
makeLink(emptylist,1,2)

######

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

emptylist={}
makeLink(emptylist,1,1)

emptylist={}
makeLink(emptylist,1,2)

emptylist={}
makeLink(emptylist,2,1)  # this is the same as on top, but a dictionary doesn't necessarily place things in order. 


makeLink(empty,1,2)

makeLink(empty,2,3)

###############
def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes [0,1,2,3,4]

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring) # 5 nodes

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 
# 5 edges


# edges1=(0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240)
# edges2=(15,31,47,63,79,95,111,127,143,159,175,191,207,223,239,255)
# 
# 
# empty={}
# 
# range(3)
# number = 9
# num_square_root = 3 
# right_side = []
# left_side = []
# bottom_row = []
# 
# for i in range(num_square_root):
# 	x = i*num_square_root-1 + num_square_root 
# 	right_side.append(x)
# right_side
# 	
# for i in range(num_square_root):
# 	x = i*num_square_root
# 	left_side.append(x)
# left_side
# 
# x = left_side[0]
# for i in range(num_square_root):
# 	y = x +1
# 	bottom_row.append(y)
# left_side
# 
# for i in range(num_square_root-1):
# 	makeLink(empty,right_side[i],right_side[i]+1)

# TODO: create a square graph with 256 nodes and count the edges 

import math

empty_list={}
def squarelinks(list, entry):
	sqrt_entry = int(math.sqrt(entry))
	for i in range(entry):
		if (i+1)%sqrt_entry != 0:
			makeLink(list, i, i+1)
		if ((i)/sqrt_entry)<(sqrt_entry-1):
			makeLink(list, i, i+sqrt_entry)

# squarelinks(empty_list,9)
squarelinks(empty_list,256)
empty_list

# input = number-1
# top_right_corner = number-1
# right_corners =[top_right_corner + input
# 
# num_squared = number^2

makeLink(empty,1,2)

makeLink(empty,2,3)

# Grid Network

# TODO: define a function countEdges

def countEdges(ring, node)
	print sum([len(ring[node]) for node in ring.keys()])/2 

	
# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
print len(movies) # 7 nodes


# How many edges in movies?
print sum([len(movies[node]) for node in movies.keys()])/2 # 10 edges


def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [] 
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms) # [Julia Roberts, Dustin Hoffman, Robert DiNero, Meryl Streep]


# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path
