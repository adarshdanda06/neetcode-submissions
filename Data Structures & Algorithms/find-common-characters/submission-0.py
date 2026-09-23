class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freqArr = []
        for word in words:
            freqDict = {}
            for letter in word:
                freqDict[letter] = freqDict.get(letter, 0) + 1
            
            freqArr.append(freqDict)
        res = []
        firstFreqDict = freqArr[0]
        for letter in firstFreqDict.keys():
            minCount = firstFreqDict[letter]
            for i in range(1, len(freqArr)):
                currFreqDict = freqArr[i]
                minCount = min(currFreqDict.get(letter, 0), minCount)

            for i in range(minCount):
                res.append(letter)
        
        return res

            