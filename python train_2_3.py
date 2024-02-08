def num_one(string, string_2):
    if string[-1] == string_2[0]:
        print(True)
    else:
        print(False)

def num_two(string):
    pos = 0
    count = 0
    for char in string:
        if char == "0":
            count += 1
            if count == 3:
                print(pos)
        pos += 1

def num_three(string):

    numbers = [int(num) for num in string.split(',')]
    print(sum(numbers))

def num_four(date_string):

    date_list = date_string.split('-')
    date_dict = {'year' : date_list[0], 'month': date_list[1], 'day': date_list[2]}
    print(date_dict)

def num_five(dict):
    dict_val = list(dict.values())
    print(set(dict_val))

num_five({
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
})