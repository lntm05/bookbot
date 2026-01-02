import sys
from stats import get_num_words, count_characters, sort_occurrences

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_occurrences = count_characters(book_text)
    char_list = sort_occurrences(char_occurrences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in char_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()