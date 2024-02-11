def num_one(string):

    word_list = string.split()

    a_words = []

    for word in word_list:

        if word[0].lower() == 'а':

            a_words.append(word)

def num_two(list):

    for i in list:
        if i <= 0:
            print(False)
            return False
    print(True)





