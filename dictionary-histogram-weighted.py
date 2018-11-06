import random
import re

histogram_dictionary = {}
def histogram(text):
    for word in text:
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1
    return histogram_dictionary

def random_word(histogram_dictionary):
    total = 0
    words_sum = sum(histogram_dictionary.values())
    random_sum = random.randint(0, words_sum - 1)
    for key, value in histogram_dictionary.items():
        total += value
        if total > random_sum:
            return key
        else:
            continue
def dictionary_test(histogram_dictionary):
    test_dictionary = {}
    for _ in range(0, 10000):
        selected_word = random_word(histogram_dictionary)
        if selected_word in test_dictionary:
            test_dictionary[selected_word] += 1
        else:
            test_dictionary[selected_word] = 1
    return test_dictionary

def file_open():
    with open('test.txt', 'r') as text:
        text_string = document_text.read().lower()
        match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
    return match_pattern

if __name__ == "__main__":
    text = file_open()
    run = histogram(text)
    print(run)
    print(random_word(run))
    print(dictionary_test(run))
