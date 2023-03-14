"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self, path):
        """Reads .txt file and displays number of words"""
        file = open(path, 'r')
        self.lst = self.read_words(file)
        print(f'[{len(self.lst)}] words read')

    def read_words(self, file):
        """Creates list from .txt file"""
        return [line for line in file]

    def random(self):
        """Returns random word from .txt file passed"""
        word = random.choice(self.lst)
        return word.strip()
        
class SpecialWordFinder(WordFinder):

    def read_words(self, file):
        """Returns random word from .txt file passed, filtered for exceptions"""
        return [char.strip() for char in file if char.strip() and not char.startswith('#')]

    
        

