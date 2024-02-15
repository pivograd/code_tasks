def num_one(integer):

    for num in str(integer):

        try:
            if last_num > int(num):
                print(False)
                return False
        except UnboundLocalError:
            pass

        last_num = int(num)
    print(True)

def num_two(list):

    while '' in list:
        list.remove('')
    print(list)

def num_three(list):
    for i in list:
        print(i)
        for num in i:
            print(num)

