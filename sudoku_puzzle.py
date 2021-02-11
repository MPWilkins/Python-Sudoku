# Create Sudoku board
board = [
		[8, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 3, 6, 0, 0, 0, 0, 0],
		[0, 7, 0, 0, 9, 0, 2, 0, 0],
		[0, 5, 0, 0, 0, 7, 0, 0, 0],
		[0, 0, 0, 0, 4, 5, 7, 0, 0],
		[0, 0, 0, 1, 0, 0, 0, 3, 0],
		[0, 0, 1, 0, 0, 0, 0, 6, 8],
		[0, 0, 8, 5, 0, 0, 0, 1, 0],
		[0, 9, 0, 0, 0, 0, 4, 0, 0]
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
            
            sb[row][col] = 0
            
    return False


def validate_board(sb, num, pos):
    # Check Row
    for i in range(len(sb[0])):
        if sb[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check Column
    for i in range(len(sb)):
        if sb[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check 3x3 
    box_x = pos[1] // 3
    box_y = pos[0] // 3
        
    for i in range(box_y * 3, box_y * 3 + 3):
        for k in range(box_x * 3, box_x * 3 + 3):
            if sb[i][k] == num and (i,k) != pos:
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