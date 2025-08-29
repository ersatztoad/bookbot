def word_counter(book_string):
    words = book_string.split()
    word_count = len(words)
    return word_count

def character_counter(book_string):
    lowercase_book_string = book_string.lower()
    char_dict = {}
    
    for char in lowercase_book_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorter(sorter_dict):
    sorter_list = []
    temp_dict = {}

    for key in sorter_dict:
        value = sorter_dict[key]
        temp_dict = {"char": key, "num": value}
        sorter_list.append(temp_dict)
        sorter_list.sort(reverse=True, key=sort_on)
    return sorter_list
    
