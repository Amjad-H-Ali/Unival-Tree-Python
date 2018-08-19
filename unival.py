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

# Wrapper function
def how_many_univals (root):
	total_count, unival = count_univals(root)
	return total_count

def count_univals (root):
	# If the root does not exist
	if (root == None):
		return(0, True)
	# Recursively check every branch and unpack return value
	left_count, left_unival = count_univals(root.left)
	right_count, right_unival = count_univals(root.right)

	# Assume is unival until one of the following coditions tells us otherwise
	is_unival = True
	# If the left root does not equal right root, not unival
	if (not left_unival or not right_unival ):
		is_unival = False
	# If the left root exist and does not equal root, then not unival
	if (root.left and root.left.value != root.value):
		is_unival = False
	# If the right root exist and does not equal root, then not unival
	if (root.right and root.right.value != root.value):
		is_unival = False
	# If still unival then add all the child branches that were unival and plus one for the tree itself
	if (is_unival):
		return (left_count + right_count + 1, True)
	# Else, just add the children roots	
	else:
		return (left_count + right_count, False)	
		




