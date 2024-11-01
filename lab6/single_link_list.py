# Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Create the LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
# Implement the Display Method
class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
# Implement the Insert Method
def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node
# Implement the Delete Method
def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
# Implement the Search Method
def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
#Implement the Reverse Method
def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


####Exercises for Students##############

# Implement a method to find the middle element of the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_middle(self):#The find_middle method initializes two pointers, slow and fast, both starting at the head of the linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
        # return the data of the slow pointer, which points to the middle element.

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Middle element:", linked_list.find_middle())  # Output should be 3

# Create a method to detect if the linked list has a cycle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def has_cycle(self):
        #The has_cycle method uses the two pointers, slow and fast, to traverse the linked list.
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # If there is a cycle, the fast pointer will eventually catch up to the slow pointer,
                # meaning they will be equal (slow == fast), and the method will return True.
                return True  # Cycle detected
        return False  # No cycle

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Create a cycle for testing
linked_list.head.next.next.next.next = linked_list.head.next  # Cycle from node 4 to node 2

print("Cycle detected:", linked_list.has_cycle())  # Output should be True
# If there is no cycle, the fast pointer will reach the end of the list 
# (i.e., fast or fast.next will become None), and the method will return False.

# Implement a method to remove duplicates from an unsorted linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_duplicates(self):
        #The remove_duplicates method iterates through each node in the linked list.
        current = self.head
        prev = None
        seen_values = set()

        while current:
            if current.data in seen_values:#seen_values set to keep track of the unique values encountered.
                # Duplicate found; remove it
                prev.next = current.next
            else:
                # New unique element
                seen_values.add(current.data)
                prev = current
                #prev.next pointer to skip the current node, effectively removing it.
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(4)
linked_list.append(3)

print("Original list:")
linked_list.print_list()

linked_list.remove_duplicates()

print("List after removing duplicates:")
linked_list.print_list()

# Add a method to merge two sorted linked lists into a single sorted linked list.
class LinkedList:
    # ... (previous code)

    @staticmethod
    def merge_sorted_lists(list1, list2):
        # Create a new linked list to store the merged result
        merged_list = LinkedList()

        # Initialize pointers for the two input lists
        current1 = list1.head
        current2 = list2.head

        # Iterate through both input lists and add the smaller value to the merged list
        while current1 and current2:
            if current1.data <= current2.data:
                # Add the current node from list1 to the merged list
                merged_list.append(current1.data)
                # Move to the next node in list1
                current1 = current1.next
            else:
                # Add the current node from list2 to the merged list
                merged_list.append(current2.data)
                # Move to the next node in list2
                current2 = current2.next

        # If there are remaining nodes in list1, add them to the merged list
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next

        # If there are remaining nodes in list2, add them to the merged list
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next

        # Return the merged list
        return merged_list

# Example usage:
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(5)

merged_list = LinkedList.merge_sorted_lists(list1, list2)

merged_list.print_list()

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.display()

ll.insert(4, 1)
ll.display()

ll.delete(2)
ll.display() 

print(ll.search(4))
print(ll.search(5))

ll.reverse()
ll.display() 