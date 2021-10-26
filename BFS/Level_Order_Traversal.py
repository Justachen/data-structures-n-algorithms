from collections import deque

# Problem Statement

# Given a binary tree, populate an array to represent its level-by-level traversal. 
# You should populate the values of all nodes of each level from left to right in 
# separate sub-arrays.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def traverse(root):
	# traverse through each level of the tree using bfs and return the path in order
	results = []
	queue = deque()
	queue.append(root)
	while queue:
		length = len(queue)
		current_row = []
		for _ in range(length):
			current_node = queue.popleft()
			current_row.append(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		results.append(current_row)
	return results


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(traverse(root)))

main()