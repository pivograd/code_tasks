def num_one(list):
    sum = 0
    for int in list:
        sum += int
    print(sum)

def num_two(list):
    sum = 0
    for int in list:
        sum += int ** 2
    print(sum)

def num_three(list):
    sum = 0
    for int in list:
        sum += int ** 0.5
    print(sum)

def num_four(list):

    sum = 0
    for i in list:
        if i > 0:
            sum += i
    print(sum)

def num_five(list):
    sum = 0
    for i in list:
        if i > 0 and i < 10:
            sum += i
    print(sum)

def num_six(string):

    list_str = list(string)
    list_str.reverse()
    for i in list_str:
        print(i)

