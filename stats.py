def count_words(book):
    word_list = book.split()
    return len(word_list)

def character_counter(text):
    lower_text = text.lower()
    char_counter = {}

    for char in lower_text:
        if char in char_counter:
            char_counter[char] += 1
        elif char not in char_counter:
            char_counter[char] = 1
    return char_counter

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    sorted_list = []

    for key in dict:
        inner_dict = {"key": key,"num": dict[key]}
        sorted_list.append(inner_dict)
    
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

