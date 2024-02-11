def num_one(string):

    vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'I', 'O', 'U', 'Y', 'E', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Е', 'Ё']

    list_string = list(string)

    for i in list_string:
        if i in vowel_letters:
            list_string.remove(i)

    print(''.join(list_string))

def num_two(set1, set2):

    print(set1.intersection(set2))

def num_three(set1, set2):

    print(set1.symmetric_difference(set2))


