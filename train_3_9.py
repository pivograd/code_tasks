def num_one(list):
    new_list = list.copy()
    for num in list:

        zero_count = 0
        for char in str(num):

            if char == '0':
                zero_count += 1
                if zero_count >= 2:
                    new_list.remove(num)

    print(new_list)

def num_two():
    set_int = set()
    for num in range(1, 1000):
        sum = 0
        for char in str(num):
            sum += int(char)
        if sum == 13:
            set_int.add(num)
    print(set_int)

