# Create Sudoku board
board = [
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
								   ]


# sb = Sudoku Board
def print_board(sb):
    
    for i in range(len(sb)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
            
        for k in range(len(sb[0])):
            if k % 3 == 0 and k != 0:
                print(" | ", end = "")
                
            if k == 8:
                print(sb[i][k])
            else:
                print(str(sb[i][k]) + " ", end = "")
            
            
def find_empty(sb):
    
    for i in range(len(sb)):
        for k in range(len(sb[0])):
            if sb[i][k] == 0:
                return (i, k) # row, col
                
# print_board(board)