class Book:
    total_boooks = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_boooks += 1

#Test 
Book.increment_book_count()
Book.increment_book_count()
print(f"Total books: {Book.total_boooks}")
