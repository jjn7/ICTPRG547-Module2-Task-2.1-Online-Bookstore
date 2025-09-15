# Import custom classes from other files
from models.book import Book
from data_structures.linked_list import DoubleLinkedList

# Main function 
def main():
    # Initialize data structures
    inventory = DoubleLinkedList()
    
    # Test with sample books
    book1 = Book(12345, "Harry Potter", "J.K. Rowling", "Fantasy", 29.99)
    book2 = Book(67890, "Animal Farm", "George Orwell", "Fiction", 19.99)
    
    # Test adding books to linked list
    print("Adding books to inventory...")
    inventory.add_book(book1)
    print(f"Added book 1. Inventory size: {inventory.size}")
    
    inventory.add_book(book2)
    print(f"Added book 2. Inventory size: {inventory.size}")
    
    # Test that head and tail are set correctly
    print(f"First book in inventory: {inventory.head.data}")
    print(f"Last book in inventory: {inventory.tail.data}")

# only run main() if this file is run directly (not if it's imported by another file)
# Every Python file has a built-in variable called __name__. Python automatically sets this variable differently depending on how the file is used.
if __name__ == "__main__":
    main()