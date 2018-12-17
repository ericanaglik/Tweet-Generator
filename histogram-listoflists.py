import random

def histogram_listoflists(file):
    text_file = open(file, 'r')

    content = text_file.read().lower().replace('\n', '')
    words = content.split(' ')
    text_file.close()


    list_of_words = []
    count = []

    for word in words:
        if word in list_of_words:
            count[list_of_words.index(word)] += 1
        else:
            list_of_words.append(word)
            count.append(1)

    histogram = []
    i = 0

    for word in list_of_words:
        histogram.append([list_of_words[i], count[i]])
        i += 1

    return histogram

if __name__ == '__main__':
    histogram_listoflists = histogram_listoflists('test.txt')
    print(histogram_listoflists)
