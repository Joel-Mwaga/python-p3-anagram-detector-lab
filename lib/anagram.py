# your code goes here!
# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  
    
    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)  
        matches = []
        
        for candidate in possible_anagrams:
            
            if sorted_word == sorted(candidate.lower()):
                matches.append(candidate)
        
        return matches