def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    length = len(file_contents.split())
    print(f"{length} words found in the document")

    letter_count = dict()
    for letter in file_contents:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1

    sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

    for letter, count in sorted_letter_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

main()