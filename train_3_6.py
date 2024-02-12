def num_one(list):

    new_list = list.copy()
    for number in list:

        if len(str(number)) > 3:

            new_list.remove(number)

    print(new_list)

def num_two(string):

    if string.isnumeric():
        print(True)
    else:
        print(False)

def num_three(integer):

    for i in str(integer):

        if not int(i) > 0:

            print(False)
            return False
    print(True)

def num_four(list1, list2):

    print(set(list1).issubset(set(list2)))


