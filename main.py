def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        words = file_content.split()
        word_count = len(words)
        print(word_count)

main()
