book_name = "books/frankenstein.txt"
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

def report(text):
    def sort_index1(tuple):
        return tuple[1]
    
    nb_words = count_words(text)
    dico_c = count_characters(text)
    list_c = []
    for pair in dico_c:
        if pair.isalpha():
            list_c.append((pair, dico_c[pair]))
    list_c.sort(reverse=True, key=sort_index1)

    print(f"--- Begin report of {book_name} ---")
    print(f"{nb_words} words found in the document")
    print()
    for (c, nb) in list_c:
        print(f"The '{c}' character was found {nb} times")
    print("--- End report ---")




def main():
    with open(book_name) as f:
        file_contents = f.read()
        report(file_contents)

if __name__ == '__main__':
    main()