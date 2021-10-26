from collections import deque

# Problem Statement

# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the 
# shortest path from the root node to the nearest leaf node.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def find_minimum_depth(root):
	# how do we go about this?
	# we need to keep track of the depth that we are at
	# we can still use a queue to keep track of the nodes in a certain level
	# condition we are looking for - if not current_node.left or not current_node.right
	# return the current depth
	# else, we just keep itereating vut we dont need to keep track of the nodes we are passing
	# just the levels

	minimum_depth = 0	
	queue = deque()
	queue.append(root)
	while queue:
		minimum_depth += 1
		length = len(queue)
		for _ in range(length):
			current_node = queue.popleft()
			if not current_node.left and not current_node.right:
				return minimum_depth
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
	return -1

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))

main()