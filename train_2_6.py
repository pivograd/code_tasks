def num_one(string):
    pos = 0
    all_pos = []
    for char in string:

        if char.isdigit():
            all_pos.append(pos)
        pos += 1
    print(all_pos)

def num_two(string):

    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()

    print(new_string)

def num_three(list):

    new_list = list[::2]
    new_list_1 = list[1::2]
    end_list = []
    for i in range(len(new_list)):
        end_list.append(int(str(new_list[i])+str(new_list_1[i])))

    print(end_list)

def num_four(string):

    new_string = ''
    list_word = string.split()
    count = 1
    for word in list_word:
        if count % 2 == 0:
            new_string += word.capitalize() + ' '
            count += 1
        else:
            new_string += word + ' '
            count += 1

    print(new_string)




