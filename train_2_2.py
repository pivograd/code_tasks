def num_one(list):
    count = 0
    for i in list:
        if i < 0:
            count += 1
    print(count)

def num_two(list):
    list_for_check = list.copy()
    for i in list_for_check:
        if i > 0:
            pass
        else:
            list.remove(i)
    print(list)

def num_three(string):
    list_string = [str for str in string]
    list_string.pop(-2)
    new_string = ''
    for char in list_string:
        new_string += char
    print(new_string)

def num_four(list):
    condition = '.html'
    check_list = list.copy()
    for string in check_list:
        if string.endswith(condition):
            pass
        else:
            list.remove(string)
    print(list)


def num_five(list):
    new_list = []
    for float in list:
        new_list.append(round(float, 1))
    print(new_list)

def num_six(dict):
    new_list = [val for val in dict.values()]
    print(new_list)

num_six({
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
})