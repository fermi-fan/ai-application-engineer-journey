# 栈
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Pop
element = stack.pop()

# Peek
top_element = stack[-1]
print("Popped element: ", element)

# isEmpty
isEmpty = not bool(stack)
print("Is stack empty? ", isEmpty)

# Size
print("Stack size: ", len(stack))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"        
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# Create a stack instance
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)
print("Popped element: ", myStack.pop())
print("Top element: ", myStack.peek())
print("Is stack empty? ", myStack.isEmpty())
print("Stack size: ", myStack.size())    

# Stack implementation using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())