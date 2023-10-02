class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.starts_with = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
            cur.starts_with += 1
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        if not cur.is_end:
            return False
        return True

