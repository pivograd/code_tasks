def num_one(string):
    pos = 0
    for char in string:
        try:
            int_char = int(char)
            print(pos)
            break
        except:
            pos += 1


def num_two(integer):
    count = 0
    for num in str(integer):
        if int(num) % 2 == 0:
            count += 1
    print(count)


def num_three(dict):

    list_keys = list(dict.keys)

    print(list_keys)

def num_four(string):

    new_string = ''

    is_odd = True

    for char in string:
        try:
            int_char = int(char)
            new_string += char
        except:
            if is_odd:
                new_string += char.upper()
                is_odd = False
            else:
                new_string += char
                is_odd = True
    print(new_string)

def num_five(string):

    new_string = ''
    list_word = string.split()
    for word in list_word:
        new_string += word.capitalize() + ' '

    print(new_string)

def num_six(date_string):

    list_date = date_string.split('-')
    list_date.reverse()
    print(tuple(list_date))

num_six('2025-12-31')