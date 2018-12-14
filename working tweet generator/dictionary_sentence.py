import sys, random, time, string

def read_text_file(text):
    with open(text) as f:
        word_data = f.read()
    return word_data
    
def tuple_convert(text_string):
    word_bank_tuple = tuple(text_string.split())
    return word_bank_tuple
    
def list_convert(text_string):
    word_bank = text_string.split()
    return word_bank
        
    
def word_count():
    try:
        count_string = str(sys.argv[1])
        return int(count_string)
    except IndexError:
        print("Error: Please enter a single integer only.")
        exit()
            
def random_sentence(word_bank, num_of_words):
    rand_sentence_string = ""
    for index in range(0, num_of_words):
        rand_item = word_bank.pop(random.randint(0, len(word_bank) - 1))
        rand_sentence_string = rand_sentence_string + " " + rand_item
    print(rand_sentence_string)
    
def get_random_sentence_tuple(word_bank_tuple, num_of_words):
    rand_string = ""
    for i in range(int(str(num_of_words))):
        rand_index = random.randint(0, len(word_bank_tuple) - 1)
        rand_word = word_bank_tuple[rand_index]
        rand_string = " ".join([rand_string, rand_word])
    return rand_string
    
def main():
    start = time.time()
    text_file = read_text_file('tswift.txt')
    text_list = tuple_convert(text_file)
    random_sentence = get_random_sentence_tuple(text_list, word_count())
    print(random_sentence)
    end = time.time()
    print(end - start)
    
if __name__ == '__main__':
    main()



