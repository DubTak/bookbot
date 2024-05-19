def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_chars = sort_char_dict(char_count)
    
    print(f'--- Begin report of {book_path} ---')
    print(f'{word_count} words found in the document\n')
    for i in sorted_chars:
        print(f"The '{i['char']}' character was found {i['count']} times")
    print('--- End report ---')
    

def get_book_text(path):    
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count_dict = {}
    for char in text.lower():
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict


def sort_on(dict):
    return dict['count']


def sort_char_dict(dict):
    list_of_dicts = []
    for k, v in dict.items():
        if k.isalpha():
            list_of_dicts.append({'char': k, 'count': v})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    

main()
