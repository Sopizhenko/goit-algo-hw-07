'''
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
'''

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def sumValues(root):
	if root is None:
		return 0
	return root.val + sumValues(root.left) + sumValues(root.right)


if __name__ == '__main__':
	r = Node(50)
	r = insert(r, 30)
	r = insert(r, 70)
	r = insert(r, 40)
	r = insert(r, 10)
	r = insert(r, 60)
	r = insert(r, 80)
	print(sumValues(r))