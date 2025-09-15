# Import custom classes from other files
from models.book import Book
from data_structures.linked_list import DoubleLinkedList
from data_structures.hash_table import HashTable

# Main function 
def main():
    # Initialize data structures
    inventory = DoubleLinkedList()
    quick_lookup = HashTable()  # Including Hash Table
    
    # Test with sample books
    book1 = Book(12345, "Harry Potter", "J.K. Rowling", "Fantasy", 29.99)
    book2 = Book(67890, "Animal Farm", "George Orwell", "Fiction", 19.99)
    book3 = Book(23456, "The Great Gatsby", "F. Scott Fitzgerald", "Historical Fiction", 24.99)
    
    # Print header
    print("Bookstore Inventory")
    print("=" * 30)

    # Add books to inventory
    inventory.add_book(book1)
    inventory.add_book(book2)
    inventory.add_book(book3)
    inventory.display_all()       # Show added books
    
    # TESTING HASH TABLE OUTPUT
    print("\n" + "=" * 30)
    print("Testing Hash Table:")
    print("=" * 30)

    quick_lookup.add_book(book1)  # Should go to position 5 (12345 % 10)
    quick_lookup.add_book(book2)  # Should go to position 0 (67890 % 10)
    quick_lookup.add_book(book3)  # Should go to position 1 (11111 % 10)
    
    # Display hash table contents
    quick_lookup.display_all()

    # Test finding books
    print("\nTesting book lookups:")
    found_book = quick_lookup.find_book(12345)
    if found_book:
        print(f"Found: {found_book}")
    else:
        print("Book not found")
    
    # Test finding non-existent book
    not_found = quick_lookup.find_book(99999)
    if not_found:
        print(f"Found: {not_found}")
    else:
        print("Book ID 99999 not found (as expected)")

# only run main() if this file is run directly (not if it's imported by another file)
# Every Python file has a built-in variable called __name__. Python automatically sets this variable differently depending on how the file is used.
if __name__ == "__main__":
    main()