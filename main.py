def count_words(text):
    count = 0
    text = text.split()
    for _ in text:
        count += 1
    return count

def count_characters(text):
    dico = {}
    for character in text:
        character = character.lower()
        if character not in dico:
            dico[character] = 0
        dico[character] += 1
    return dico


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))

if __name__ == '__main__':
    main()