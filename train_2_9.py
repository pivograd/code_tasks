def num_one(list):

    for i in range(0, 100, 2):

        list.append(i)

    print(list)

def num_two(list):

    list.reverse()
    for i in list:
        print(i)

def num_three(string, string_2):
    res = {}
    for i in range(len(string)):
        res[string[i]] = string_2[i]
    print(res)




