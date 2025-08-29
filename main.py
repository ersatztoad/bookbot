import sys
from stats import word_counter
from stats import character_counter
from stats import sorter

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    print("----------- Word Count ----------")
    cnt = word_counter(text)
    print(f"Found {cnt} total words")

    print("--------- Character Count -------")
    character_dictionary = character_counter(text)
    sorted_list = sorter(character_dictionary)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
        else:
            pass


main()