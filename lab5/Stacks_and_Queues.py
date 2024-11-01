#  Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.peek())  
print(stack.size()) 

# Implementing a Queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front())  
print(queue.size())  

#Solving Practical Problems
#--Balanced Parentheses
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

print(is_balanced("((()))")) 

#--Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

print(reverse_string("Hello, World!"))  

#---- Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed

## Implement a function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    # Stack to store operands
    stack = []
    
    # Define operators and their corresponding lambda functions for easy evaluation
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y  
    }
    
    # Process each token in the postfix expression
    for token in expression.split():
        if token.isdigit(): 
             # Check if the token is an operand
            stack.append(int(token))
        elif token in operators: 
            # Token is an operator
            # Pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Evaluate the operation and push the result back onto the stack
            result = operators[token](operand1, operand2)
            stack.append(result)
    
    # The final result is the only item left on the stack
    return stack.pop() if stack else None

expression = "3 4 + 2 * 7 /"  # Example: (3 + 4) * 2 / 7
print("Result:", evaluate_postfix(expression))

##Create a function that uses two stacks to implement a queue.
class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue
        self.stack2 = []  # Stack for dequeue

    def enqueue(self, item):
        # Push item onto the first stack
        self.stack1.append(item)

    def dequeue(self):
        # If both stacks are empty, the queue is empty
        if not self.stack1 and not self.stack2:
            return "Queue is empty"

        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the top element from stack2 (front of the queue)
        return self.stack2.pop()

    def is_empty(self):
        # Queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

    def peek(self):
        # Peek at the front element without dequeuing it
        if not self.stack1 and not self.stack2:
            return "Queue is empty"
        
        if not self.stack2:
            # Transfer elements if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

# Testing the queue implementation
queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeue:", queue.dequeue())  
print("Peek:", queue.peek())      
print("Dequeue:", queue.dequeue())  
print("Is empty:", queue.is_empty()) 
print("Dequeue:", queue.dequeue())  
print("Is empty:", queue.is_empty()) 

##Use a queue to implement a basic task scheduler that processes tasks in the order they were added.
from collections import deque
import time

class TaskScheduler:
    def __init__(self):
        # Queue to store tasks
        self.task_queue = deque()
    
    def add_task(self, task, duration):
        """Add a task to the scheduler with a specified duration in seconds."""
        self.task_queue.append((task, duration))
        print(f"Task '{task}' added with duration {duration} seconds.")

    def run(self):
        """Process tasks in the order they were added."""
        print("Starting task scheduler...")
        while self.task_queue:
            # Dequeue the next task
            task, duration = self.task_queue.popleft()
            print(f"Processing task: {task}")
            
            # Simulate task execution
            time.sleep(duration)
            print(f"Task '{task}' completed.")
        
        print("All tasks completed.")

# Testing the TaskScheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1", 2)
scheduler.add_task("Task 2", 3)
scheduler.add_task("Task 3", 1)

##Implement a function that uses a stack to convert infix expressions to postfix
def infix_to_postfix(expression):
    # Defining precedence and associativity of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L'}
    
    # Stack for operators and list for output
    stack = []
    output = []
    
    # Process each token in the expression
    for token in expression.split():
        if token.isalnum(): 
         # If the token is an operand (number/variable), add's to output
            output.append(token)
        elif token in precedence:
        # If the token is an operator
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and associativity[token] == 'L'))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':  
        # If the token is an open parenthesis, push to stack
            stack.append(token)
        elif token == ')': 
        # If the token is a close parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
            # Pop the '(' but don't add it to the output

    # Pop all remaining operators from the stack to the output
    while stack:
        output.append(stack.pop())
    
    return " ".join(output)

# Test the function
expression = "3 + 4 * 2 / ( 1 - 5 )"
print("Infix:", expression)
print("Postfix:", infix_to_postfix(expression))
