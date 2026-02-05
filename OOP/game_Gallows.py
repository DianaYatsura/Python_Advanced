# The basic premise of the game Gallows is to follow two rules:
# First character of next word must match last character of previous word.
# The word must not have already been said.
# Below is an example of a Gallows game:
# ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!
# ['motive', 'beach']  # invalid! - beach should start with "e"
# ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
# Write a Gallows class that has two instance variables:
# words: a list of words already said.
# game_over: a boolean that is true if the game is over.
# and two instance methods:
# play: a method that takes in a word as an argument and checks if it is valid (the word should follow rules #1 and #2 above).
# If it is valid, it adds the word to the words list, and returns the words list.
# If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
# restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false. It should return "game restarted".

class Gallows:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if word in self.words:
            self.game_over = True
            return 'game over!'

        if self.words:
            last_word = self.words[-1]
            last_letter = last_word[-1]
            if word[0] != last_letter:
                self.game_over = True
                return 'game over!'

        self.words.append(word)
        return self.words


    def restart(self):
        self.game_over = False
        self.words = []
        return "game restarted"



my_gallows = Gallows()
print(my_gallows.play('apple')) # ['apple']
print(my_gallows.play('ear')) # ['apple', 'ear']
print(my_gallows.play('rhino')) # ['apple', 'ear', 'rhino']
print(my_gallows.words) # ['apple', 'ear', 'rhino']
print(my_gallows.restart()) # "game restarted"
print(my_gallows.words) #[]

