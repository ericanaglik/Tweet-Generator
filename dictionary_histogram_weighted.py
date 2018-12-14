import random
from get_corpus import read_file



def histogram(words_list):
    histogram_dict = {}
    for word in words_list:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
    return histogram_dict

def generate_random_word(histogram_dict):
    total = 0
    # Finding total frequency of all words in the histogram.
    total_frequency_list = histogram_dict.values()
    total_frequency_number = 0
    for frequency in total_frequency_list:
        total_frequency_number += frequency

    random_count = random.randint(0, total_frequency_number-1)

    for key,value in histogram_dict.items():
        total += value
        if total > random_count:
            return key

def dictionary_test(histogram_dictionary):
    test_dictionary = {}
    for _ in range(0, 10000):
        selected_word = generate_random_word(histogram_dictionary)
        if selected_word in test_dictionary:
            test_dictionary[selected_word] += 1
        else:
            test_dictionary[selected_word] = 1
    return test_dictionary

def random_word_histogram(words_list, histogram_dict):
    random_word_list = list()
    for i in range(1000):
        random_word_list.append(generate_random_word(histogram_dict))
    weighted_histogram = histogram(random_word_list)
    return weighted_histogram

# def file_open():
#     document_text = 'test.txt'
#     with open('test.txt', 'r') as text:
#         text_string = document_text.read().lower()
#         match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
#     return match_pattern

def main():
    file_data = read_file("tswift.txt")
    histogram_dict = histogram(file_data)
    random_word_weighted = generate_random_word(histogram_dict)
    random_word_weighted_dict = random_word_histogram(file_data,histogram_dict)
    print(random_word_weighted)
    print(random_word_weighted_dict)


if __name__ == "__main__":
    main()
