import random
import sys

def rearrange_words():
    # turns input words into list
    input_words = sys.argv[1:]
    words = []
    for word in input_words:
        rand_index = random.randint(0, len(input_words) -1)
        list = input_words[rand_index]
        words.append(list)
        result = ' '.join(words)
    return result

if __name__ == '__main__':
    rearrange = rearrange_words()
    print(rearrange)
