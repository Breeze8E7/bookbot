def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print (get_word_count(file_contents))

main()