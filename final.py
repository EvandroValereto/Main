import book, os, csv

SECURITY_KEY = '2130'  # used to enter privilaged mode, used in print_menu
DEFAULT_MENU = {'1':'Search for books', '2':'Borrow a book', '3':'Return a book', '0':'Exit the system'}
ADMIN_MENU = {'4':'Add a book', '5':'Remove a book', '6':'Print catalog', '0':'Exit the system'}
def load_books(filename:str, books:list): # returns # of books loaded
    """
    Load books from a CSV file into a list.
    Parameters:
        filename (str): The pathname to the CSV file.
        books (list): The list to store the loaded books.
    Returns:
        int: The number of books loaded.
    """
    num_books_loaded = 0
    # opens the CSV file for reading
    file = open(filename, 'r', newline='')
    #creates a CSV reader object
    reader = csv.reader(file)
    # iterates over each row in the CSV file
    for row in reader:
        #Checks if the row has all the required fields(5)
        if len(row) == 5:
            #extract data from the row
            isbn, title, author, genre, available = row
            #create a Book object and appendit to the list of books
            books.append(book.Book(isbn, title, author, int(genre), available.lower() == 'true'))
            # increments the count of loaded books
            num_books_loaded += 1
    file.close()
    return num_books_loaded

def save_books(filename:str, books:list): # returns # of books saved
    """
    Save books from a list to a CSV file.

    Parameters:
        filename (str): The pathname to the CSV file.
        books (list): The list containing the books to save.
    Returns:
        int: The number of books saved.
    """ 
    num_books_saved = 0
    # opens the CSV file for writing
    file = open(filename, 'w', newline='')
    # creates a CSV writer object
    writer = csv.writer(file)
    #iterates over each book in the list
    for book in books:
        # writes the book content ot the CSV file
        writer.writerow([book.get_isbn(), book.get_title(), book.get_author(), book.get_genre(), book.get_available()])
        #increments  the count of saved books
        num_books_saved += 1
    file.close()
    return num_books_saved  
def print_books(books:list):
    """
    Print the details of all books in the list.

    Parameters:
        books (list): The list containing the books to print.
    """
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("{:s} {:s} {:s} {:s} {:s}".format("-"*14, "-"*25, "-"*25, "-"*20, "-"*12,))
    # interates over each book in the list and print its details
    for book in books:
        print(book)
