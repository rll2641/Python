class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 삽입
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # 단순 주소 저장
        node.word = True # 마지막 알파벳의 word를 true로 저장. -> 단어완성
    
    # 단어 존재 여부 판별
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word # true or false
    
    # 해당 문자열로 시작하는 단어가 존재하는지 여부
    def startsWitch(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

    
    