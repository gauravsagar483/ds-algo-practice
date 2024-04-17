from LRU import log

import json


class Trie:

    def __init__(self):
        self.root = {}

    @log
    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]

        cur["*"] = ""
        return json.dumps(self.root, indent=2)

    @log
    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur:
                return False
            cur = cur[char]

        return "*" in cur

    @log
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True


trie = Trie()
trie.insert("apple")
trie.insert("apps")
trie.insert("appstr")
trie.insert("appstr3")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
