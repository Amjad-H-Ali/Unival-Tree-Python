print('Unival Tree!')

# Tree class to instantiate Node Tree object
class Tree:
	def __init__(self,value):
		self.value = value

		self.left = None

		self.right = None

# Instance of Tree Class (Our Node)
root = Tree(5)
root.left = Tree(1)
root.right = Tree(5)
root.left.left = Tree(5)
root.left.right = Tree(5)
root.right.right = Tree(5)

print(root.value)	




