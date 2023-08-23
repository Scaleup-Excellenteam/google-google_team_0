import re


class TrieNode:
    def __init__(self, word: str = "", filename: str = ""):
        self.word = str(word).lower()
        self.is_end = False
        self.counter = 0
        self.children = {}
        self.filename = filename



class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def clean_line(line: str) -> list[str]:
        return re.sub(r'[^a-zA-Z]+', ' ', line).lower().split()

    def insert(self, line: str, filename: str):
        node = self.root
        for word in self.clean_line(line):
            if word not in node.children:
                node.children[word] = TrieNode(word, filename)
            node = node.children[word]
        node.is_end = True
        node.counter += 1
        node.filename = filename

    def search(self, prefix: str, last_word_prefix: str):
        pass


