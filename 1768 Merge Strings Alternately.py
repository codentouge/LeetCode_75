class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            output += word1[i] + word2[i]
            
        output += word1[min_length:] + word2[min_length:]

        return output