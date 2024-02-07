def num_one(string):
    if len(string) > 1:
        print(string[-2])

def num_two(x, y):
    if x % y == 0:
        print('True')
    else:
        print("False")

def num_three(string):
    chur_list = [ chur for chur in string]
    print(chur_list)

def num_four(list):
    print(list[2:-1])

def num_five(dict):
    year = dict['year']
    month = dict['month']
    day = dict['day']

    print(f'{year}-{month}-{day}')
