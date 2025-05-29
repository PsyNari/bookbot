from stats import count_words
from stats import count_characters
from stats import sorted_dictionary
import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]



    with open(file_path) as f:
        book_text = f.read()
    characters = count_characters(book_text)
    words = count_words(book_text)
    sorted_characters = sorted_dictionary(characters)
    print(f"============ BOOKBOT ============\n"
          f"Analyzing book found at {file_path}...\n"
          f"----------- Word Count ----------\n"
          f"Found {words} total words\n"
          f"--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    

main()
