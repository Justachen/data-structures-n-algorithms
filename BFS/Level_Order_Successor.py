from collections import deque

# Problem Statement

# Given a binary tree and a node, find the level order successor of the given node in 
# the tree. The level order successor is the node that appears right after the given 
# node in the level order traversal.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def find_successor(root, target):
	queue = deque()
	queue.append(root)
	found = False
	while queue:
		current_node = queue.popleft()
		if current_node.left:
			queue.append(current_node.left)
		if current_node.right:
			queue.append(current_node.right)
		if current_node.val == target:
			break

	return queue[0] if queue else None

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	result = find_successor(root, 12)
	if result:
		print(result.val)
	result = find_successor(root, 9)
	if result:
		print(result.val)

main()