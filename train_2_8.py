def num_one(list):

    for i in range(1, 10):
        list.append(i)

    print(list)

def num_two(string):

    count = 0
    for i in string:
        if not i.islower():
            count += 1
            if count > 2:
                print(False)
                return False
    print(True)
    return True

def num_three(list):

    new_list = [int(i) for i in list]

    print(new_list)

num_three(['1', '2'])
