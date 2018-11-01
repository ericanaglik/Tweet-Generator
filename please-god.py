import random
words = [1,2,3,4,5,6,7,8]
new_words = ["one", "two", "red", "blue", "fish"]
frequency = [1, 1, 1, 1, 4]
denominator = int(len(words))
frequency_percent = []

for i in frequency:
    frequency_percent.append((i/denominator))

print(random.choices(new_words,frequency_percent,k = 8))
