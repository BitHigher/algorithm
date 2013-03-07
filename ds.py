root = {}

def find(u):
	if u not in root:
		root[u] = u
		return u
	
	ru = root[u]
	if ru == u:
		return u
	else:
		# compress the path
		_root = find(ru)
		root[u] = _root
		return _root

def union(u, v):
	ru = find(u)
	rv = find(v)
	if ru != rv:
		root[rv] = ru
