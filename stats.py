def count_words(book_text):
    words = book_text.split()
    number_of_words = len(words)
    return number_of_words

def count_characters(book_text):
    current_characters = {}
    for character in book_text:
        character = character.lower()
        if character not in current_characters:
            current_characters[character] = 1
        else:
            current_characters[character] += 1
    return current_characters

def sorted_dictionary(current_characters):
    sorted_characters = sorted(current_characters.items(), key=lambda item: item[1], reverse=True)
    sorted_items = []
    for char, num in sorted_characters:
        if char.isalpha():
            sorted_items.append({"char": char, "num": num})
    return sorted_items

