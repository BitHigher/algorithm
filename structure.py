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

class priority_queue:
	class node:
		def __init__(self, key, value, index=0):
			self.key = key
			self.value = value
			self.index = index

	
	def __init__(self, array):
		''' each element of array is a pair (key, value) '''
		self.array = [0]
		self.table = {}
		for (key, value) in array:
			if self.table.has_key(key): continue
			n = self.node(key, value, len(self.array))
			self.array.append(n)
			self.table[key] = n

		self.size = len(self.array)-1
		self.make_heap()

	def assign(self, index, node):
		node.index = index
		self.array[index] = node
	
	def compare(self, n1, n2, less=True):
		if less:
			return n1.value < n2.value
		else:
			return n1.value > n2.value


	def top_down(self, index):
		self.array[0] = self.array[index]

		while index*2 <= self.size:
			minson = index*2
			if minson != self.size and self.compare(self.array[minson+1], self.array[minson]):
				minson += 1

			if self.compare(self.array[minson], self.array[0]):
				self.assign(index, self.array[minson])
				index = minson
			else:
				break
		self.assign(index, self.array[0])

	def make_heap(self):
		for i in range(self.size/2, 0, -1):
			self.top_down(i)

	def delete_min(self):
		if(self.size == 0):
			return None
		value = self.array[1].value
		key = self.array[1].key
	
		self.table.pop(key)	
		self.assign(1, self.array[self.size])
		self.size -= 1
		self.top_down(1)
		
		return value

	def bottom_up(self, index):
		self.array[0] = self.array[index]
		j = index
		while j/2 > 0 and self.compare(self.array[0], self.array[j/2]):
			self.assign(j, self.array[j/2])
			j /= 2

		self.assign(j, self.array[0])

	def insert(self, pair):
		k, v = pair
		if self.table.has_key(k):
			return False

		self.size += 1
		n = self.node(k, v, self.size)
		self.table[k] = n
		if len(self.array) < self.size+1:
			self.array.append(n)
		else:
			self.array[self.size] = n

		self.bottom_up(self.size)

	def set_value(self, key, value):
		if not self.table.has_key(key):
			return False

		n = self.table[key]
		if n.value == value:
			return
		if n.value < value:
			n.value = value
			self.top_down(n.index)
		else:
			n.value = value
			self.bottom_up(n.index)
