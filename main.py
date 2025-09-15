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
    
    #TEST PRINT BOOK PROPERTIES
    print("Bookstore Inventory")
    print("=" * 30)
    print("Testing Book Properties:")
    print(f"Book 1 Title: {book1.title}")
    print(f"Book 1 Price: ${book1.price}")
    print(f"Book 1 Genre: ${book1.genre}")
    print()

# only run main() if this file is run directly (not if it's imported by another file)
# Every Python file has a built-in variable called __name__. Python automatically sets this variable differently depending on how the file is used.
if __name__ == "__main__":
    main()