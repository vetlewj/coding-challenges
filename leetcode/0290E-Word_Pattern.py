class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordlist = [w for w in s.split(" ")]
        pattern_word_match = {}
        if len(wordlist) != len(pattern): 
            return False
        for i, j in enumerate(pattern):
            print(pattern_word_match.values())
            if (j not in pattern_word_match.keys()) and (wordlist[i] not in pattern_word_match.values()):
                pattern_word_match[j] = wordlist[i]
            else: 
                if pattern_word_match.get(j) != wordlist[i]: 
                    return False
        return True