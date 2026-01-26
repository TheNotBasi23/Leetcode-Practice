from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ingridentsWordOne = set([char for char in word1])
        ingridentsWordTwo = set([char for char in word2])
        if ingridentsWordTwo != ingridentsWordOne:
            return False



        firstWord = Counter(word1)
        secondWord = Counter(word2)

        def getFrequency(wordDict):
            freq = {}
            for key in wordDict:
                freq[wordDict[key]] = freq.get(wordDict[key], 0 ) + 1
            return freq

        freq1 = getFrequency(firstWord)
        freq2 = getFrequency(secondWord)
        if len(freq1) != len(freq2):
            return False
        else:
            for key in freq1:
                if freq1[key] != freq2.get(key,0):
                    return False
            return True

