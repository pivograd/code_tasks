def num_one():
    for i in range (1, 101):
        print(i)

def num_two():
    for i in range (-100, 1):
        print(i)

def num_three():
    for i in range (100, 0, -1):
        print(i)

def num_four():
    for i in range (1, 101):
        if i % 2 == 0:
            print(i)

def num_five():
    for i in range (1, 101):
        if i % 3 == 0:
            print(i)

def num_six(list):

    list_2 = [list[elem] for elem in range(-2, 0)]
    print(list_2)

def num_seven(string):

    print(set(string))


