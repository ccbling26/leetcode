from typing import List


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for c in word:
            k = ord(c) - ord("a")
            if node.children[k] is None:
                node.children[k] = Trie()
            node = node.children[k]
        node.isEnd = True

    def track(self, node: "Trie", c: str):
        k = ord(c) - ord("a")
        if node is None or node.children[k] is None:
            return None, False
        node = node.children[k]
        return node, node.isEnd


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d = [0] + [n + 1] * n
        trie = Trie()
        for word in dictionary:
            trie.insert(reversed(word))
        for i in range(1, n + 1):
            d[i] = d[i - 1] + 1
            node = trie
            for j in range(i - 1, -1, -1):
                node, ok = trie.track(node, s[j])
                if ok:
                    d[i] = min(d[i], d[j])
        return d[n]
