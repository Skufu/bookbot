import os

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print(f"Total word count:{word_count}")

    for char, count in char_count.items():
        print(f"the '{char} character appears {count}' times")
    
    return word_count
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

main()



