class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

wordDict = [];
wordFile = open('words.txt','r');
for word in wordFile:
	wordDict.append(word.rstrip("\r\n"));
print wordDict