import sys, random, string
from dictogram import Dictogram

from sampling import weighted_choice


class markov(dict):
    
    def __init__(self, word_list = None, order = 1):
        super(markov, self).__init__()
        
        self.order = order
        
    def create_markov(self, word_list):
        
        order = self.order
        
        for i in range(len(word_list) - self.order):
            key = tuple(word_list[i: i + order])
            value = word_list[i + order]
            self.check_key(key,value)
            
    def check_key(self, key, value):
        if key in self:
            self[key].add_count(value)
        else:
            self[key] = Dictogram([value])
            
    def generate_sentence(self, text_list, count=10):
        random_string = ""
        random_key = random.choice(list(self))
        second_word = weighted_choice(self[random_key])
        random_string = random_string + ' '.join(random_key) + ' ' + second_word
        
        for i in range(count - self.order - 1):
            
            temporary_list = list(random_key)
            temporary_list.append(second_word)
            temporarily_list = temporary_list[1:]
            random_key = tuple(temporary_list)
            
            try:
                second_word = weighted_choice(self[random_key])
            except KeyError:
                random_key = random.choice(list(self))
                second_word = weighted_choice(self[random_key])
                
            while second_word == None:
                second_word = weighted_choice(self[random_key])
                print(second_word)
                
            random_string = random_string + " " + second_word
        
        return random_string
        
def read_text_file(text):
    with open(text) as f:
        word_data = f.read()
    return word_data
    
def list_convert(text_string):
    word_list = text_string.split()
    return word_list

def main():
    text_file = read_text_file("tswift.txt")
    text_list = list_convert(text_file)
    markov_chain = markov(text_list, 2)
    markov_chain.create_markov(text_list)
    string = markov_chain.generate_sentence(text_file, 3)
    
    
    return string 
    
if __name__ == '__main__':
    main()
    main_file = main()
    print(main_file)  
        