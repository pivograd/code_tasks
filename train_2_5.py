def num_one(string):
    pos = 0
    all_pos = []
    for char in string:

        if char == '0':
            all_pos.append(pos)
        pos += 1
    print(set(all_pos))

def num_two(string):

    new_string = ''
    count = 1
    for char in string:
        if count % 3 == 0:
            count += 1

        else:
            new_string += char
            count += 1
    print(new_string)

def num_three(list):

    sum_1 = 0
    sum_2 = 0
    is_odd = False
    for num in list:

        if is_odd:
            sum_1 += num
            is_odd = False
        else:
            sum_2 += num
            is_odd = True

    print(sum_2/sum_1)

def num_four(list_date):

    list_date.reverse()
    print(tuple(list_date))


