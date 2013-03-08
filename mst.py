import numpy
import structure

def kruskal(graph):
	''' graph is undirected and represented by a n*n matrix '''
	# find all edges
	edges = []
	n = graph.shape[0]
	for i in range(n):
		for j in range(i+1, n):
			if graph[i, j] > 0:
				edges.append(((i, j), graph[i, j]))

	edges = sorted(edges, key=lambda x:x[1])
	
	# construct the mst from minmum edge
	mst = numpy.zeros((n, n))
	n_edges = 0
	ds = structure.disjoint_set()
	for (e, w) in edges:
		if ds.find(e[0]) != ds.find(e[1]):
			mst[e] = w
			ds.union(e[0], e[1])
			n_edges += 1
			if(n_edges == n-1):
				return mst
	return mst

def prime(graph):
	n = graph.shape[0]
	mst = numpy.zeros((n, n))
	selected = []
	unselected = set([i for i in range(n)])
	distance = [(numpy.inf, i) for i in range(n)]

	# set the distance of vertex 0 to 0
	distance[0] = (0, 0)
	heap = structure.heap(distance, key=lambda x:x[0])
