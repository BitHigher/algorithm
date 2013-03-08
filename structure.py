class disjoint_set:
	def __init__(self):
		self.root = {}
	
	def find(self, u):
		if u not in self.root:
			self.root[u] = u
			return u

		ru = self.root[u]
		if ru == u:
			return u
		else: 
			# compress the path
			_root = self.find(ru)
			self.root[u] = _root
			return _root

	def union(self, u, v):
		ru = self.find(u)
		rv = self.find(v)
		if ru != rv:
			self.root[rv] = ru

class heap:
	def __init__(self, items, key=None):
		self.array = [0]
		for item in items:
			self.array.append(item)
		self.size = len(self.array)-1
		
		if key == None: self.key = lambda x:x
		else: self.key = key
		
		self.make_heap()
	
	def make_heap(self):
		for i in range(self.size/2, 0, -1):
			self.top_down(i)

	def top_down(self, index):
		self.array[0] = self.array[index]
		while index*2 <= self.size:
			minson = index * 2
			if minson != self.size and self.key(self.array[minson]) > self.key(self.array[minson+1]):
					minson += 1
			if self.key(self.array[minson]) < self.key(self.array[0]):
				self.array[index] = self.array[minson]
			else:
				break
			index = minson
		self.array[index] = self.array[0]

	def delete_min(self):
		if(self.size < 1):
			return None

		value = self.array[1]
		self.array[1] = self.array[self.size]
		self.size -= 1
		self.top_down(1)
		return value

	def bottom_up(self, index):
		self.array[0] = self.array[index]
		while index/2 > 0 and self.key(self.array[0]) < self.key(self.array[index/2]):
			self.array[index] = self.array[index/2]
			index /= 2
		self.array[index] = self.array[0]

	def insert(self, value):
		self.size += 1
		if len(self.array) < self.size+1:
			self.array.append(value)
		else:
			self.array[self.size] = value

		self.bottom_up(self.size)

