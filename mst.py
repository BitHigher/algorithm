import numpy
import structure

def kruskal(graph):
	''' graph is undirected and represented by a n*n matrix '''
	# find all edges
	edges = []
	n = graph.shape[0]
	for i in range(n):
		for j in range(i+1, n):
			if graph[i, j] < numpy.inf:
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
	unselected = set([i for i in range(1, n)])
	distance = [graph[0, i] for i in range(n)]
	prev = {}
	for i in unselected:
		prev[i] = 0

	while len(unselected) > 0:
		# find minmum distance
		# may be replaced by heap
		mini = numpy.inf
		minidx = 0
		for i in unselected:
			if distance[i] < mini:
				mini = distance[i]
				minidx = i
		unselected.discard(minidx)
		mst[minidx, prev[minidx]] = mini

		# update the distance of vertics to minindex
		for i in range(n):
			if graph[minidx, i] < distance[i]:
				distance[i] = graph[minidx, i]
				prev[i] = minidx

	return mst
