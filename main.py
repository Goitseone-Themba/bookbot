def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text) 
    characters = character_count(text)
    print_report(book_path, word_count, characters)

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
        words = text.split()
        return len(words)

def character_count(text):
    character_map = {}
    words = text.casefold()
    for word in words:
        for c in word:
            if c in character_map:
                character_map[f"{c}"] += 1
            else:
                character_map[f"{c}"] = 1

    return character_map

def print_report(path, word_count, characters):
    all_keys = list(characters)
    keys = []

    for k in all_keys: 
        if k.isalpha():
            keys.append(k)

    for h in range(0, len(keys)):
        for i in range(0, len(keys)-1):
            if characters[keys[i]] < characters[keys[i+1]]:
                buffer = keys[i]
                keys[i] = keys[i+1]
                keys[i+1] = buffer

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for c in keys:
            print(f"The '{c}' character was found {characters[c]} times")
    print("--- End report ---")

main()
