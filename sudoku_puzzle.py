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
def print_board(su):
    
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
            
        for k in range(len(su[0])):
            if k % 3 == 0 and k != 0:
                print(" | ", end = "")
                
            if k == 8:
                print(su[i][k])
            else:
                print(str(su[i][k]) + " ", end = "")
            
            
def find_empty(su):
    
    for i in range(len(su)):
        for k in range(len(su[0])):
            if su[i][k] == 0:
                return (i, k) # row, col
                
# print_board(board)