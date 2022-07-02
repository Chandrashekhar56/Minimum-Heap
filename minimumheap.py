
import sys
class Maximum_Heap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.ArrayOfHeap = [0] * (self.maxsize + 1)
		self.ArrayOfHeap[0] = sys.maxsize
		self.FRONT = 1

	def Node_parent(self, position):
		return position-1 // 2

	def Node_leftChild(self, position):
		return 2 * position

	def Node_rightChild(self, position):
		return (2 * position) + 1

	def CheckLeafFunction(self, position):

		if position >= (self.size//2) and position <= self.size:
			return True
		return False

	def SwapFunction(self, first_position, second_position):
		self.ArrayOfHeap[first_position], self.ArrayOfHeap[second_position] = (self.ArrayOfHeap[second_position],self.ArrayOfHeap[first_position])

	def FindMaxHeap(self, position):
		if not self.CheckLeafFunction(position):
			if (self.ArrayOfHeap[position] < self.ArrayOfHeap[self.Node_leftChild(position)] or
				self.ArrayOfHeap[position] < self.ArrayOfHeap[self.Node_rightChild(position)]):
				if (self.ArrayOfHeap[self.Node_leftChild(position)] >
					self.ArrayOfHeap[self.Node_rightChild(position)]):
					self.SwapFunction(position, self.Node_leftChild(position))
					self.FindMaxHeap(self.Node_leftChild(position))

				else:
					self.SwapFunction(position, self.Node_rightChild(position))
					self.FindMaxHeap(self.Node_rightChild(position))

	def ElementInsert(self, value):
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.ArrayOfHeap[self.size] =value

		current = self.size

		while (self.ArrayOfHeap[current] < self.ArrayOfHeap[self.Node_parent(current)]):
			self.SwapFunction(current, self.Node_parent(current))
			current = self.Node_parent(current)

	def DisplayFunction(self):
		for x in range(1, (self.size // 2) + 1):
			print(" Parent Node : " + str(self.ArrayOfHeap[x]))
			print("Left Child : " + str(self.ArrayOfHeap[2 * x]) +
			" Right Child : " + str(self.ArrayOfHeap[2 * x + 1]))

	def extractMaximuHeap(self):
		remove = self.ArrayOfHeap[self.FRONT]
		self.ArrayOfHeap[self.FRONT] = self.ArrayOfHeap[self.size]
		self.size -= 1
		self.FindMaxHeap(self.FRONT)

		return remove
if __name__ == "__main__":

	print('The maxHeap is ')

	m = Maximum_Heap(15)
	m.ElementInsert(1)
	m.ElementInsert(2)
	m.ElementInsert(3)
	m.ElementInsert(4)
	m.ElementInsert(5)
	m.ElementInsert(6)
	m.ElementInsert(7)
	m.ElementInsert(8)
	m.ElementInsert(9)

	m.DisplayFunction()

	print("The Max val is " + str(m.extractMaximuHeap()))
