def num_one(list):
    condition = 'http://.'
    check_list = list.copy()
    for string in check_list:
        if string.startswith(condition):
            pass
        else:
            list.remove(string)
    print(list)

def num_two(string):
    str_list = [i for i in string]
    try:
        print(str_list.index('0'))
    except ValueError:
        pass

def num_three(list, delete):

    while delete in list:
        list.remove(delete)
    print(list)

def num_four():

    for number in range(10, 1000):
        str_number = str(number)
        if int(str_number[0])+int(str_number[1]) == 5:
            print(number)

def num_five(string):

    new_string = ''
    for char in string:
        if char not in new_string:
            new_string += char

    print(new_string)

num_five('abcdeabc')