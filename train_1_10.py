def num_one(string):

    print(string[::2])

def num_two(integer):

    list_int = [i for i in str(integer)]
    list_int.reverse()
    for i in list_int:
        print(i)
