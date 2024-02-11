def num_one():

    num_list = [num for num in range(1, 10, 2)]

    print(num_list)


def num_two(tuple1, tuple2):

    combo_tuple = tuple1 + tuple2

    print(combo_tuple)

def num_three(dict1, dict2):

    combo_dict = {}

    combo_dict.update(dict1)
    combo_dict.update(dict2)

    print(combo_dict)

def num_four(list):

    sum1 = 0
    sum2 = 0

    for i in range(len(list)):

        if i+1 > len(list)/2:

            sum2 += list[i]
        else:

            sum1 += list[i]

    print(sum1/sum2)

