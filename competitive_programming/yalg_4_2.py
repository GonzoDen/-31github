def is_safe(board, row, col, N): 
    # Check if there is a queen in the same column 
    for i in range(row): 
        if board[i][col] == 1: 
            return False 
 
    # Check upper diagonal on the left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 
 
    # Check upper diagonal on the right side 
    for i, j in zip(range(row, -1, -1), range(col, N)): 
        if board[i][j] == 1: 
            return False 
 
    return True 
 
def solve_n_queens(N): 
    board = [[0 for _ in range(N)] for _ in range(N)] 
    count = [0]  # Store the count as a mutable list 
 
    solve_util(board, 0, N, count) 
     
    return count[0] 
 
def solve_util(board, row, N, count): 
    if row == N: 
        count[0] += 1 
        return 
 
    for i in range(N): 
        if is_safe(board, row, i, N): 
            board[row][i] = 1 
 
            solve_util(board, row + 1, N, count) 
 
            board[row][i] = 0 
 
N = int(input()) 
total_solutions = solve_n_queens(N) 
print(total_solutions)щ