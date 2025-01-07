class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def search(board, word, w, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            letter = board[i][j]
            if letter != word[w]:
                return 

            w += 1
            if w >= len(word):
                return True

            board[i][j] = ''
            if search(board, word, w, i+1, j) or search(board, word, w, i-1, j) or search(board, word, w, i, j+1) or search(board, word, w, i, j-1):
                return True
            board[i][j] = letter
            
            return False
        
        if not board or not board[0]: return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, word, 0, i, j):
                    return True
        return False