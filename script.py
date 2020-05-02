import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']
def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

#Comment out the bubble sort attempt and try quicksort
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in sort_3:
  print(len(book['author_lower']) + len(book['title_lower']))

#Python’s built-in comparison operators compare letters lexicographically based on their Unicode code point. You can determine the code point of characters using Python’s built-in ord function
#print(ord("a"))
#print(ord(" "))
#print(ord("A")) 
