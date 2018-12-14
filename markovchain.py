# def markov_dict(self, tokens):
#     markov_dict = {}
#     for index, token_key in enumerate(tokens)
#         if index == len(tokens) - 1: break
#         if token_key not in markov_dict:
#             markov_dict[token_key] = {tokens[index + 1]: 1}
#         else:
#             next_token = tokens[index + 1]
#             if next_token not in markov_dict[token_key]:
#                 markov_dict[token_key][next_token] = 1
#             else:
#                 markov_dict[token_key][next_token] += 1
#     return markov_dict
#
#     def tweet_generator(self, markov_dict):
#         #empty list or sentence variable to push
#         temporary_maryk
import re #cleans text and gets text only in quotations
import random
from dictogram import Dictogram


class MarkovChain():
	def __init__(self, corpus, order):
		# import arguments
		self.corpus = corpus
		self.order = order
		# initialize 'empty' variables
		self.word = ''
		self.phrase = []
		self.dict = {}
		self.types = 0
		self.tokens = 0
		# call saveDict
		self.saveDict()

	def saveWord(self):
		'''
			Saves a complete stored word into the phrase, then resets the stored word.
			The results are saved in self.word
			---
			When a word is being formed:
			> its stored in a string in self.word
			When a word is complete:
			> its put into the self.phrase array, then reset.
		'''
		if len(self.phrase)  < self.order:
			self.phrase += [self.word]
		if len(self.phrase) == self.order:
			self.savePhrase()
		self.word = ''

	def savePhrase(self):
		'''
			Saves a complete stored phrase into the dictionary, then resets the stored phrase.
			The results are saved in self.phrase
			---
			When a phrase is being formed:
			> its stored in an array in self.phrase
			When a phrase is complete:
			> its put into the self.dict dictionary, then reset.
		'''
		phrase = tuple(self.phrase)
		if phrase in self.dict:
			self.dict[phrase] += 1
		else:
			self.dict[phrase]  = 1
			self.types += 1
		self.tokens  += 1
		del self.phrase[0]

	def saveDict(self):
		'''
			Creates a markov chain by looping through each letter in the corpus.
			The results are saved in self.dict
			---
			When a dictionary is being formed:
			> its stored in a histogram in self.dict
			When a dictionary is complete:
			> its put into the self.dict dictionary.
		'''
		self.dict = {}
		for grapheme in self.corpus:
			if grapheme == ' ': # this can be improved greatly
				self.saveWord()
			else:
				self.word += grapheme
		self.saveWord()


if __name__ == '__main__':
	fishy = "One fish two fish, red fish blue fish"
	Model = MarkovChain(fishy, 1)
	print(f"DICTIONARY:\n{Model.dict}\n")
	print(f"UNIQUE TYPES: {Model.types}\n")
	print(f"TOTAL TOKENS: {Model.tokens}\n")
