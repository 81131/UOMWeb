class SinglyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendOperation(self, data):
        if self.next:
            self.next.appendOperation(data)
        else:
            self.next = SinglyLinkedList(data)
    
    def __repr__(self):
        # Represent the linked list as a string for debugging
        return f"SinglyLinkedList({self.data})" + (f" -> {repr(self.next)}" if self.next else "")

    def __str__(self):
        # Recursive approach for string conversion
        if self.next is None:
            return str(self.data)
        return f"{self.data} -> {self.next}"


# Test the corrected implementation
linkedList1 = SinglyLinkedList(89)
linkedList1.appendOperation(50)
linkedList1.appendOperation(70)

# Outputs
print(linkedList1)  # Should print: 89 -> 50 -> 70

# Accessing data
print(linkedList1.data)  # Output: 89
print(linkedList1.next.data)  # Output: 50
print(linkedList1.next.next.data)  # Output: 70
