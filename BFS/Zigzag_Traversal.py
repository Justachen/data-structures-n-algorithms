from collections import deque

# Problem Statement#

# Given a binary tree, populate an array to represent its zigzag level order traversal. 
# You should populate the values of all nodes of the first level from left to right, 
# then right to left for the next level and keep alternating in the same manner for the 
# following levels.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def traverse(root):
	results = []
	queue = deque()
	queue.append(root)
	lefttoright = True

	while queue:
		length = len(queue)
		current_row = deque()
		for _ in range(length):
			current_node = queue.popleft()

			# adding the next level of the queue
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)

			# determining whether to zig or zag
			if lefttoright:
				current_row.append(current_node.val)
			else:
				current_row.appendleft(current_node.val)

		results.append(current_row)		
		lefttoright = not lefttoright

	return results

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("Zigzag traversal: " + str(traverse(root)))

main()