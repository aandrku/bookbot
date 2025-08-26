from stats import count_words, count_chars, get_dicts
import sys

def sort_on(items):
    return items["count"]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(path, words_count, char_occurences):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for oc in char_occurences:
        if oc["char"].isalpha():
            print(f"{oc["char"]}: {oc["count"]}")

    print("============= END ===============")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    contents = get_book_text(path)
    words_count = count_words(contents)
    chars_count = count_chars(contents)
    dicts = get_dicts(chars_count)
    dicts.sort(reverse=True, key=sort_on)

    print_report(path, words_count, dicts)
    
main()

