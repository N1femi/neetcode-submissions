class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        . for empty spots

        I can loop through each row and keep track on numbers seen, I'd also do the same thing. as a column in place
        If i find a number already hashed in lookup table then I return false on the spot

        for 3 by 3 we can do a secondary loop by 3 increments and check box, or in place
        """
        col_hash = defaultdict(set)
        row_hash = defaultdict(set)
        squares_hash = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in row_hash[row] or 
                board[row][col] in col_hash[col] or 
                board[row][col] in squares_hash[(row // 3, col // 3)]):
                   return False

                row_hash[row].add(board[row][col])
                col_hash[col].add(board[row][col])
                squares_hash[(row // 3, col // 3)].add(board[row][col])

        return True

                    
                    
        