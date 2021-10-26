from collections import deque

# Problem Statement

# Given a binary tree, populate an array to represent its level-by-level traversal in 
# reverse order, i.e., the lowest level comes first. You should populate the values of 
# all nodes in each level from left to right in separate sub-arrays.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def traverse(root):
	# return an array of the tree from left to right starting from the bottom to the top
	results = deque()
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
		results.appendleft(current_row)


	return results

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Reverse level order traversal: " + str(traverse(root)))

main()
