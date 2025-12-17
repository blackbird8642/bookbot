import sys
from stats import count_words, character_counter,sorted_list

def get_book_text(book_path):

    with open(book_path) as book:
        book_text = book.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path=sys.argv[1]
    book = get_book_text(book_path)
    num_words = count_words(book)
    char_counter = character_counter(book)
    char_list = sorted_list(char_counter)


    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for char in char_list:
        if char["key"].isalpha():
            print(f"{char["key"]}: {char["num"]}")
    print("============= END ===============")


main()