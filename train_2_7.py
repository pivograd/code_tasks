def num_one(char):

    if char.islower():
        print('Нижний регистр')

    elif char.isupper():
        print('Верхний регистр')

def num_two(integer):
    new_string = ''
    for num in str(integer):
        if int(num) % 2 == 0:
            new_string += num
    print(int(new_string))

def num_three(date_tuple):

    date_dict = {'year': date_tuple[0], 'month': date_tuple[1], 'day': date_tuple[2]}
    print(date_dict)

num_three(('2025', '12', '31'))
