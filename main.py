import stats

def main():
    book_path = "./books/frankenstein.txt" # hard-coded relative path to the book .txt file

    with open(book_path) as f: # with operator will close the .txt file when the operation is completed for memory conservation
        book_string = f.read() # .read() function takes the .txt file and converts it into a string which is assigned to the book_string variable

    word_count = stats.word_count(book_string) # imports the word_count function from stats.py and uses book_string as the input
    char_count = stats.count_chars(book_string) # imports count_chars from stats.py and uses book_string as input
    char_list = stats.sort_char_dict(char_count) # imports sort_char_dict from stats.py and uses char_count dictionary as input

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in char_list:
        char = dict["char"]
        count = dict["count"]
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
