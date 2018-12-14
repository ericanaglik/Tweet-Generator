import sys, string
from dictionary_sentence import read_text_file, list_convert

def histogram(source_text):
    histogram_dict = {}
    for word in source_text:
        if histogram_dict.get(word) is None:
            histogram_dict[word] = 1
        else:
            histogram_dict[word] += 1
    return histogram_dict
    
def word_types(histogram_dict):

    count = 0 
    for key in histogram_dict:
        count += 1
    return count
    
def frequency(word, histogram):
    count = 0
    for key in histogram: 
        if word == key:
            count = histogram[key]
    return count
    
def main():
    file_text = read_text_file('tswift.txt')
    text_list = list_convert(file_text)
    text_list[:] = [i.translate(str.maketrans('','',string.punctuation)) for i in text_list]
    my_histogram = histogram(text_list)
    print(my_histogram)
    
    number_of_word_types = unique_wirds(my_histogram)
    print("The Number of unique words is: {}".format(word, word_count))
    
    if __name__ == '__main__':
        main()