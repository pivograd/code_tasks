def num_one(integer):
    divisor_list = []
    i = 1
    while i < integer//2 + 1:
        if integer % i == 0:
            divisor_list.append(i)
        i += 1
    divisor_list.append(integer)
    print(divisor_list)

def num_two():

    for i in range(10, 1000):

        if int(str(i)[0]) % 2 == 0:
            print(i)

def num_three(list):
    print(sum(sum(list, [])))



def num_four(dict):

    sum = 0
    for value in dict.values():
        for val in value.values():
            sum += val

    print(sum)
