class Book:
    def __init__(self, book_id, title, author, publication_year, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed = False
        self.borrow_count = 0

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class LibraryManager:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, book):
        """
        Add a book to the library

        Args:
            book (Book): Book to add

        Returns:
            bool: True if book was added, False if book with same ID already exists
        """
        if not isinstance(book, Book):
            raise TypeError("Object must be of type Book")

        if book.book_id in self.books:
            return False

        self.books[book.book_id] = book
        return True

    def get_book(self, book_id):
        """
        Get a book by its ID

        Args:
            book_id: ID of the book to get

        Returns:
            Book or None: Book if found, None otherwise
        """
        return self.books.get(book_id)

    def remove_book(self, book_id):
        """
        Remove a book from the library

        Args:
            book_id: ID of the book to remove

        Returns:
            bool: True if book was removed, False if book wasn't in the library
        """
        if book_id not in self.books:
            return False

        if self.books[book_id].is_borrowed:
            raise ValueError("Cannot remove a borrowed book")

        del self.books[book_id]
        return True

    def borrow_book(self, book_id, borrower_id):
        """
        Borrow a book

        Args:
            book_id: ID of the book to borrow
            borrower_id: ID of the borrower

        Returns:
            bool: True if book was borrowed, False otherwise
        """
        if book_id not in self.books:
            raise ValueError("Book not found in library")

        book = self.books[book_id]

        if book.is_borrowed:
            return False

        book.is_borrowed = True
        book.borrow_count += 1

        if borrower_id not in self.borrowed_books:
            self.borrowed_books[borrower_id] = []

        self.borrowed_books[borrower_id].append(book_id)
        return True

    def return_book(self, book_id, borrower_id):
        """
        Return a borrowed book

        Args:
            book_id: ID of the book to return
            borrower_id: ID of the borrower

        Returns:
            bool: True if book was returned, False otherwise
        """
        if book_id not in self.books:
            raise ValueError("Book not found in library")

        if borrower_id not in self.borrowed_books or book_id not in self.borrowed_books[borrower_id]:
            raise ValueError("Book was not borrowed by this borrower")

        book = self.books[book_id]

        if not book.is_borrowed:
            return False

        book.is_borrowed = False
        self.borrowed_books[borrower_id].remove(book_id)

        # Clean up empty borrower entries
        if not self.borrowed_books[borrower_id]:
            del self.borrowed_books[borrower_id]

        return True

    def search_books(self, criteria):
        """
        Search for books based on criteria

        Args:
            criteria (dict): Dictionary with search criteria
                             (title, author, year_from, year_to, genre)

        Returns:
            list: List of books matching criteria
        """
        results = []

        for book in self.books.values():
            matches = True

            if 'title' in criteria and criteria['title'].lower() not in book.title.lower():
                matches = False

            if 'author' in criteria and criteria['author'].lower() not in book.author.lower():
                matches = False

            if 'year_from' in criteria and book.publication_year < criteria['year_from']:
                matches = False

            if 'year_to' in criteria and book.publication_year > criteria['year_to']:
                matches = False

            if 'genre' in criteria and book.genre != criteria['genre']:
                matches = False

            if 'available_only' in criteria and criteria['available_only'] and book.is_borrowed:
                matches = False

            if matches:
                results.append(book)

        return results

    def get_statistics(self):
        """
        Get library statistics

        Returns:
            dict: Dictionary with statistics
        """
        total_books = len(self.books)
        borrowed_count = sum(1 for book in self.books.values() if book.is_borrowed)
        available_count = total_books - borrowed_count

        # Count books by genre
        genres = {}
        for book in self.books.values():
            if book.genre not in genres:
                genres[book.genre] = 0
            genres[book.genre] += 1

        # Find most popular books (by borrow count)
        popular_books = sorted(
            self.books.values(),
            key=lambda book: book.borrow_count,
            reverse=True
        )[:5]  # Top 5

        return {
            "total_books": total_books,
            "available_books": available_count,
            "borrowed_books": borrowed_count,
            "borrowers_count": len(self.borrowed_books),
            "genres": genres,
            "popular_books": popular_books
        }