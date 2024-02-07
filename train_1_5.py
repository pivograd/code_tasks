def num_one():

    sum=0
    for i in range (1, 100):
        sum += i
    print(sum)

def num_two():

    sum=0
    for i in range (1, 100):
        if i % 2 == 0:
         sum += i
    print(sum)

def num_three():

    sum=0
    for i in range (1, 100):
        if i % 2 == 0:
            pass
        else:
         sum += i
    print(sum)

def num_four(x, y):

    print(x%y)

def num_five(list):

    print(list[0::2])

num_five([1, 2, 3, 4, 5, 6])