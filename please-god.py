import random
words = [1,2,3,4,5,6,7,8]
new_words = ["one", "two", "red", "blue", "fish"]
frequency = [1, 1, 1, 1, 4]
denominator = int(len(words))
frequency_percent = []

for i in frequency:
    frequency_percent.append((i/denominator))

print(random.choices(new_words,frequency_percent,k = 1))

def frequency_tester():
    i = 0
    blue = 0
    fish = 0
    red = 0
    two = 0
    one = 0

    while i <= 10000:
        selection = random.choices(new_words,frequency_percent,k = 1)
        if 'blue' in selection:
            blue += 1
        elif 'fish' in selection:
            fish += 1
        elif 'red' in selection:
            red +=1
        elif 'two' in selection:
            two += 1
        elif 'one' in selection:
            one +=1
        i += 1

    print("Blue => " + str(blue) + "\n fish => " + str(fish) + "\n red => " + str(red) + "\n two => " + str(two) + "\n one => " + str(one))

frequency_tester()
