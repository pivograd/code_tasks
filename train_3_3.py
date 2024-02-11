def num_one(integer):

    for i in str(integer):

        if int(i)%2 == 0:
            print(False)
            return False

    print(True)
    return True

def num_two(string):

    string_list = list(string)
    string_list.reverse()
    new_string = ''.join(string_list)

    if new_string == string:
        print(True)
    else:
        print(False)

def num_three(set1, set2):

    combo_set = set1.union(set2)

    print(combo_set)

