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
        # Create a new node and link it
        new_node = Node(book)
        
        if self.head is None: #Check if the list is empty

            # First book in the list - set both head and tail to this node    
            self.head = new_node
            self.tail = new_node

        else:   #List has books - add new book to the end and connect current last book
            self.tail.next = new_node   # Old tail points forward
            new_node.prev = self.tail   # New node points back

            self.tail = new_node    #Update tail to point to our new book (now the last one)

        self.size += 1      # Increase book Count
    
    # Remove book by ID
    def remove_book(self, book_id):
        # - finds and removes the book
        pass

    # Show all books in the inventory
    def display_all(self):
        # Goes through list and prints books
        pass