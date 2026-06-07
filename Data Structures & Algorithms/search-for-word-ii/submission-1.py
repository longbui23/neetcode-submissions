class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 

class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        root = TrieNode()

        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        res = []

        def dfs(i, j, node):
            if node.word:
                res.append(node.word)
                node.word = None  

            if i < 0 or j < 0 or i >= m or j >= n:
                return

            char = board[i][j]
            if char not in node.children:
                return

            board[i][j] = "#" 

            next_node = node.children[char]

            dfs(i + 1, j, next_node)
            dfs(i - 1, j, next_node)
            dfs(i, j + 1, next_node)
            dfs(i, j - 1, next_node)

            board[i][j] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res