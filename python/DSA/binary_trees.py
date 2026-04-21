class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=',')  # Process the current node
    preOrderTraversal(node.left)  # Traverse left subtree
    preOrderTraversal(node.right)  # Traverse right subtree

preOrderTraversal(root)
print()  # For a new line after traversal

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)  # Traverse left subtree
    print(node.data, end=',')  # Process the current node
    inOrderTraversal(node.right)  # Traverse right subtree

inOrderTraversal(root)
print()  # For a new line after traversal

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)  # Traverse left subtree
    postOrderTraversal(node.right)  # Traverse right subtree
    print(node.data, end=',')  # Process the current node

postOrderTraversal(root)
print()  # For a new line after traversal


binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

print("Pre-order Traversal:", pre_order(0))
print("In-order Traversal:", in_order(0))
print("Post-order Traversal:", post_order(0))