def num_one():

    num_list = [num for num in range(1, 7)]
    print(num_list)

def num_two(list1, list2):


    list1.extend(list2)

    print(list1)

def num_three(list):

    sum = 0

    for i in range(int(len(list)/2)):

        sum += list[i]

    print(sum)

