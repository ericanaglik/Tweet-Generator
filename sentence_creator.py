from tweetgenerator import Markov_nth_order
from dictionary_histogram_weighted import histogram, random_word_histogram
from get_corpus import read_file

def main():
    word_list = read_file("tswift.txt")
    list_len = len(word_list)
    markov = Markov_nth_order(order=3)

    markov.create_dict_of_dict(word_list)
    sentence_list = markov.generate_random_sentence(word_list, 20)
    new_sentence_list = " ".join(sentence_list)

    print(markov.order)
    histogram_dict = histogram(sentence_list)
    print(histogram_dict)
    print(new_sentence_list)
    return sentence_list

if __name__ == '__main__':
    main()
