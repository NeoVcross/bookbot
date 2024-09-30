def count_words(text):
    count = 0
    text = text.split()
    for _ in text:
        count += 1
    return count



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

if __name__ == '__main__':
    main()