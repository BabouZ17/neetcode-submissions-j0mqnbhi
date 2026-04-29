class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        wordToPattern, patternToWord = {}, {}
        for p, word in zip(pattern, words):
            if p in patternToWord and patternToWord[p] != word:
                return False
            if word in wordToPattern and wordToPattern[word] != p:
                return False

            patternToWord[p] = word
            wordToPattern[word] = p
        return True
        
            
