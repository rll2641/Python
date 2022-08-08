# 단어 리스트에서 word[i] + word[j]가 팰린드롬이 되는 모든 인덱스 조합출력(i,j)
words = ["abcd", "dcba", "lls", "s", "sssll"]

# 브루트 포스
def palindromePairs(words):
    
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    
    return output

# 트라이
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_id = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def is_palindrome(word):
        return word == word[::-1]
    
    def insert(self, index, word):
        node = self.root
        
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_id.append(index)
            node = node.children[char]
        node.word_id = index
    
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
            