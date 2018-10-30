import re
import string
frequency = {}
first_list = []
second_list = []
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
    first_list.append(word)
for word in match_pattern:
    second_list.append(int(frequency[word]))

zipped = zip(first_list, second_list)

please = list(set(zipped))

print(dict(please))












# def open_file():
#
#     f = open('source_text.txt', 'r')
#     words_list = f.readlines()
#     f.close()
#
#     split_words_list = words_list[0].split(' ')
#
# def histogram():
#
#     for i in range (len(split_words_list) -1):
#         word_count = 1
#         if split_words_list[i] == split_words_list[i+1]:
#             word_count += 1
#         else:
#             word_count = 1
#
#     return str(i) and str(word_count)
#
# def run_histogram():
#     histogram = []
#
#     open_file()
#
#     while source_text.txt has words left:
#         histogram()
#
#
#     print new list
#
