"""
Generator function randomWord has as an argument list of words. It should return any random word
from this list. Each time words are different until the end of the list is reached. Then words
are taken from the initial list again.
For example if list = ['book', 'apple', 'word']
books = randomWord(list)
then possible output example
first call of next(books) returns apple
second call of next(books) returns book
third call of next(books) returns word
fourth call of next(books) returns book
"""
import random


def randomWord(word_list):
    if not word_list:
        while True:
            yield None

    local_list = word_list.copy()
    while True:
        random.shuffle(local_list)
        for word in local_list:
            yield word


list = ['book', 'apple', 'word']
books = randomWord(list)
print(next(books)) #book
print(next(books)) #word
print(next(books)) #apple
print(next(books)) #book
print(next(books)) #apple
print(next(books)) #word
emptyRandom = randomWord([])
print(next(emptyRandom)) #None