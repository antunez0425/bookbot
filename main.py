import sys

def read_book(path):
    book = ""
    with open(path) as f:
        book = f.read()


    return book

def count_words(book):

    book = book.split()

    #print(f"Number of words: {len(book)}")

    return len(book)

def count_characters(book):

    book = book.lower()

    chars = {}

    for letter in book:
        chars[letter] = chars.get(letter, 0) + 1

    #print(chars)

    return chars

def sort_chars(char_count):
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

def main(args):
    path = "books/frankenstein.txt"

    book = read_book(path)

    print(f"--- Begin report of {path} ---")

    word_count = count_words(book)

    print(f"{word_count} words found in the document\n")

    char_count = count_characters(book)

    char_count = sort_chars(char_count)

    char_count = {k: v for k, v in char_count.items() if k.isalpha()}

    for k, v in char_count.items():
        print(f"The '{k}' character was found {v} times")

    print("--- End Report ---")

if __name__ == "__main__":
    main(sys.argv[1:])