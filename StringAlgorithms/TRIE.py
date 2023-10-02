class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        dummy = self.root
        for i in range(len(word)):
            if word[i] not in dummy:
                dummy[word[i]] = {}
            dummy = dummy[word[i]]
            if "sw" not in dummy:
                dummy["sw"] = 1
            else:
                dummy["sw"] += 1
        if "ew" not in dummy:
            dummy["ew"] = 1
        else:
            dummy["ew"] += 1

    def search(self, word: str) -> bool:
        dummy = self.root
        for i in range(len(word)):
            if word[i] not in dummy:
                return False
            dummy = dummy[word[i]]
        return "ew" in dummy

    def startsWith(self, prefix: str) -> bool:
        dummy = self.root
        for i in range(len(prefix)):
            if prefix[i] not in dummy:
                return False
            dummy = dummy[prefix[i]]
        return True

    def countWordsEqualTo(self, word: str) -> int:
        dummy = self.root
        for i in range(len(word)):
            if word[i] not in dummy:
                return 0
            dummy = dummy[word[i]]
        if "ew" not in dummy:
            return 0
        return dummy["ew"]
    
    def countWordsStartingWith(self, word: str) -> int:
        dummy = self.root
        for i in range(len(word)):
            if word[i] not in dummy:
                return 0
            dummy = dummy[word[i]]
        if "sw" not in dummy:
            return 0
        return dummy["sw"]
    
    def erase(self, word: str) -> None:
        dummy = self.root
        for i in range(len(word)):
            if word[i] not in dummy:
                return
            dummy = dummy[word[i]]
            dummy["sw"] -= 1
        if dummy["ew"] > 0:
            dummy["ew"] -= 1

def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("apple")
    trie.insert("apps")
    trie.insert("apps")
    print(trie.countWordsEqualTo("apples"))
    print(trie.countWordsStartingWith("bp"))

if __name__ == "__main__":
    main()
    