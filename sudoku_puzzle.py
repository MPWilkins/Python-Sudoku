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

def solve_sudoku(sb):
    find = find_empty(sb)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1, 10):
        if validate_board(sb, i, (row, col)):
            sb[row][col] = i
            
            if solve_sudoku(sb):
                return True
            
            sb[row][col]
            
    return False


def validate_board(sb, num, pos):
    # Check Row
    for i in range(len(sb[0])):
        if sb[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check Column
    for i in range(len(sb[0])):
        if sb[i][pos[0]] == num and pos[0] != i:
            return False
        
    # Check 3x3 
    box_x = pos[1] // 3
    box_y = pos[0] // 3
        
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sb[i][j] == num and (i,j) != pos:
                    return False
                
    return True


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
            
    return None
                
print_board(board)
solve_sudoku(board)
print("______________________________")
print_board(board)