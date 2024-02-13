def num_one(list, integer):

    new_list = list.copy()

    for i in list:
        if not integer % i == 0:
            new_list.remove(i)

    print(new_list)

def num_two(list):

    new_list = []

    for i in list:


        if len(str(i)) == 1:
            new_list.append(i)
            new_list.append(i)
        else:
            new_list.append(i)

    print(new_list)

def num_three(int1, int2):

    int_intersection_list = []

    for num in str(int2):
        if num in str(int1):
            int_intersection_list.append(int(num))

    print(int_intersection_list)

def num_four(integer):

    pos = 0
    list_pos = []

    for i in str(integer):

        if i == '3':
            list_pos.append(int(pos))
        pos += 1

    print(list_pos[1:-1])

def num_five(list):
    new_list = list.copy()
    for num in list:
        numbers = ''
        for i in str(num):
            if not i in numbers:
                numbers += i
        if len(numbers) < 2:
            new_list.remove(num)

    print(new_list)

def num_six(lst1, lst2):
    if len(lst1) > len(lst2):
        new_list = lst1[0:len(lst2)]
        print(new_list, lst2)
    elif len(lst2) > len(lst1):
        new_list = lst2[0:len(lst1)]
        print(new_list, lst1)
    else:
        print(lst1, lst2)

def num_seven(list1):
    new_list = []
    for num in list1:
        list_num = list(str(num))
        list_num.reverse()
        new_list.append(int(''.join(list_num)))
    print(new_list)





