# Node class represents one book in linked list
class Node:
    def __init__(self, data):
        self.data = data    # The actual book object stored in node
        self.prev = None    # Pointer to the previous node in the list
        self.next = None    # Pointer to the next node in the list

# DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None    # Points to the first node in the list
        self.tail = None    # Points to the last node in the list
        self.size = 0       # Track how many books stored
    
    # Add new book to list
    def add_book(self, book):
        # - creates new node and links it
        pass
    
    # Remove book by ID
    def remove_book(self, book_id):
        # - finds and removes the book
        pass

    # Show all books in the inventory
    def display_all(self):
        # Goes through list and prints books
        pass