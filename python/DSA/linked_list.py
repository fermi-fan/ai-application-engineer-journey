# 单链表实现
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode is not None:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("null")

# 双链表实现
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = DoubleNode(3)
node2 = DoubleNode(5)
node3 = DoubleNode(13)
node4 = DoubleNode(2)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("\nForward traversal:")
currentNode = node1
while currentNode :
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

print("\nBackward traversal:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

# 循环单链表
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = CircularNode(3)
node2 = CircularNode(5)
node3 = CircularNode(13)
node4 = CircularNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")

# 循环双向链表
class CircularDoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = CircularDoubleNode(3)
node2 = CircularDoubleNode(5)
node3 = CircularDoubleNode(13)
node4 = CircularDoubleNode(2)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node1
node1.prev = node4

print("\nForward traversal:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")
print("\nBackward traversal:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev
while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("...")