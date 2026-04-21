# 链表操作
# Traverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

node1 = Node(7)
node2 = Node(12)
node3 = Node(9)
node4 = Node(4)
node5 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverse_linked_list(node1)

# Delete a node from a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

def delete_node(head, key):
    
    if head == key:
        return head.next

    current_node = head
    while current_node.next and current_node.next != key:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5    

print("Before deletion:")
traverse_linked_list(node1)

# Delete node4
node1 = delete_node(node1, node4)

print("\nAfter deletion:")
traverse_linked_list(node1)

# 插入节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

def insert_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node

    current_node = head
    for _ in range(position - 2):
        if current_node is None:
            raise IndexError("Position out of bounds")
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverse_linked_list(node1)
new_node = Node(11)
node1 = insert_node(node1, new_node, 2)    
print("List after insertion:")
traverse_linked_list(node1)