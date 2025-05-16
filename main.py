from stats import count_words
from stats import count_chars
from stats import sorted_char_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

 
def main():
    
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ")
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_counts = count_chars(text)
    listed_char_count = sorted_char_count(char_counts)
    print("--------- Character Count -------")
    for x in listed_char_count:
       char = x["char"]
       if char.isalpha():
           print(f"{char}: {x['num']}")
 
    


if __name__ == "__main__":
    main()