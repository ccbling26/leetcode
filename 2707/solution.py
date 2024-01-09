from typing import List


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = True
    
    def insert(self, word: str):
        node = self
        for c in word:
            k = ord(c) - ord("a")
            if self.children[k] is None:
                self.children[k] = Trie()
            node = self.children[k]
        node.isEnd = True

    def track(self, node: "Trie", k: int):
        if node is None or node.children[k] is None:
            return None, False
        node = node.children[k]
        return node, node.isEnd


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d = [n + 1] * (n + 1)
        d[0] = 0
        trie = Trie()
        for e in dictionary:
            trie.insert(reversed(e))
        for i in range (1, n + 1):
            d[i] = d[i - 1] + 1
            node = trie
            for j in range(i - 1, -1, -1):
                node, ok = trie.track(node, s[j])
                if ok:
                    d[i] = min(d[i], d[j])
        return d[n]
