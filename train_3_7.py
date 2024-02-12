def num_one(string):

    word_list = string.split()
    new_string = ''
    for word in word_list:
        new_string += word[0:-1] + word[-1].upper() + ' '

    print(new_string)

def num_two(string):

    if not string.isnumeric():
        print(False)
        return False

    for char in string:

        if int(char) % 2 != 0:
            print(False)
            return False

    print(True)

def num_three(str1, str2):

    print(set(str1).intersection(set(str2)))

def num_four(string):

    word_list = string.split()
    new_string = ''
    for word in word_list:
        if len(word)>3:
            new_string += word + ' '
        else:
            new_string += word.upper() + ' '
    print(new_string)

num_four('a bc def ghij')
