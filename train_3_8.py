def num_one(list):

    for num in list:
        if not '3' in str(num):
            print(False)
            return False
    print(True)

def num_two(string):

    int_list_str = string.split(',')

    int_list = [int(num) for num in int_list_str]

    print(max(int_list))

def num_three(kebab_case_string):

    snake_case_string = kebab_case_string.replace('-', '_')

    print(snake_case_string)

def num_four(snake_case):

    words_list = snake_case.split('_')

    camel_case_string = words_list[0] + ''.join(word.capitalize() for word in words_list[1:])

    print(camel_case_string)

def num_five(camel_case):

    words_list = []
    current_word = ''

    for char in camel_case:

        if char.isupper():
            words_list.append(current_word)
            current_word = char.lower()

        else:
            current_word += char

    words_list.append(current_word)
    snake_case = '_'.join(words_list)
    print(snake_case)


