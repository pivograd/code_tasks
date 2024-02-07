def num_one(dict):
    sum = 0
    for i in dict.values():
        sum += i
    print(sum)

def num_two(dict):
    sum = 0
    for i in dict.values():
        sum += i ** 2
    print(sum)

def num_three(string):

    print(list(string))

def num_four(integer):
    list_int = [int(i) for i in str(integer)]
    print(list_int)

def num_five(integer):

    list_int = [i for i in str(integer)]
    list_int.reverse()
    string_int = ''
    for i in list_int:
        string_int += i
    print(int(string_int))

def num_six(integer):
    list_int = [int(i) for i in str(integer)]
    print(sum(list_int))

num_six(12345)
