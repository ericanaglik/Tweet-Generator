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

frequencies = list(set(zipped))

print(dict(frequencies))
