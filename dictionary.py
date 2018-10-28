import random
from sys import argv
i = 0
user_input = int(argv[1])
//choose a random word from words.txt
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    split_words_list = words_list[0].split(' ')
    secret_word = random.choice(split_words_list)
    return secret_word

//prints random words as many times as user asks
while i < user_input:
    print(load_word())
    i += 1
