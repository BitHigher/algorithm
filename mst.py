import numpy
import ds

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
	mst = numpy.zeros((n, n), dtype='int')
	n_edges = 0
	for (e, w) in edges:
		if ds.find(e[0]) != ds.find(e[1]):
			mst[e] = w
			ds.union(e[0], e[1])
			n_edges += 1
			if(n_edges == n-1):
				return mst
	return mst

def prime(graph):
	pass
	# TODO
