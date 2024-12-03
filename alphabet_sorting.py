def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)


def get_char_count(file_contents):
    letter_dict = {}
    for char in file_contents:
        lowered = char.lower()
        if lowered in letter_dict:
            letter_dict[lowered] += 1
        else:
            letter_dict[lowered] = 1
    return letter_dict



def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{get_word_count(file_contents)} words found in the document")
    char_count = get_char_count(file_contents)
    for char in sorted(char_count):
        if char.isalpha():
            print(f"The '{char}' was found {char_count[char]} times")
    print ("--- End report ---")

main()