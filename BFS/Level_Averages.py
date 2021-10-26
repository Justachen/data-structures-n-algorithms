from collections import deque

# Problem Statement

# Given a binary tree, populate an array to represent the averages of all of its levels.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def find_level_averages(root):
	results = []
	queue = deque()
	queue.append(root)

	while queue:
		level_average = 0 
		length = len(queue)

		for _ in range(length):
			current_node = queue.popleft()
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
			level_average += current_node.val

		level_average = level_average / length
		results.append(level_average)

	return results

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.left.right = TreeNode(2)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level averages are: " + str(find_level_averages(root)))

main()