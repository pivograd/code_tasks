def num_one(string):

    count = 0

    for i in string:

        if i.isalpha():
            count += 1
            if count > 3:
                print(False)
                return False
    print(True)
    return True

def num_two(integer):

    list_int = [int(i) for i in str(integer)]

    list_int.reverse()

    for i in list_int:
        if i % 2 == 0:
            print(i)
            return i


def num_three(string):

    new_string = ''

    list_word = string.split()

    for word in list_word:
        for i in range(len(word)):
            if i == 0:
                new_string += '!'
            else:
                new_string += word[i]
        new_string += ' '
    print(new_string)

def num_four(list):

    list_int = [int(i) for i in list]

    print(sum(list_int))

num_four(['1', '2', '3', '4', '5'])