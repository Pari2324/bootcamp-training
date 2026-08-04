#maximum number of words found in sentences
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words=0
        for i in sentences:
            count = (len(i.split()))
            if count >= max_words:
                max_words = count
        return max_words

        #time complexity = o(n)
        #space complexity = o(1)