def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(get_resport_on_char_dict(book_path, num_words, chars_dict))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    cnt = {}
    lower_text = text.lower()
    for c in text:
        lowered = c.lower()
        cnt[lowered] = cnt.get(lowered, 0) + 1
    
    return cnt

def get_resport_on_char_dict(book_path, num_words, chars_dict):
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{num_words} words found in the document\n"
    report += "\n"
    
    for c in chars_dict:
        if c.isalpha():
            report += f"The '{c}' character was found {chars_dict[c]} times\n"
    report += "--- End report ---\n"

    return report

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
