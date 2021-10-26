from __future__ import print_function
from collections import deque

# Problem Statement#

# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to a null node.

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

	def print_level_order(self):
		nextLevelRoot = self
		while nextLevelRoot:
			current = nextLevelRoot
			nextLevelRoot = None
			while current:
				print(str(current.val) + " ", end='')
				if not nextLevelRoot:
					if current.left:
						nextLevelRoot = current.left
					elif current.right:
						nextLevelRoot = current.right
				current = current.next
			print()

def connect_level_order_siblings(root):
	# so as we are traversing through each row, we want to check connect each node in the rows 
	# from left to right with the final one pointing at none
	# traverse normally, we dont't need to save anything just make the connections

	queue = deque()
	queue.append(root)
	while queue:
		length = len(queue)
		prev = None
		for _ in range(length):
			current_node = queue.popleft()
			if prev:
				prev.next = current_node
			prev = current_node
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()