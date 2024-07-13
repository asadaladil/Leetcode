def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    r,c=len(board),len(board[0])
    boxes={}
    cols={}
    rows={}
    for i in range(r):
        for j in range(c):
            if i not in rows:
                rows[i]=[]
            if j not in cols:
                cols[j]=[]
            R=int(i/3)*3
            C=int(j/3)
            I=R+C
            if I not in boxes:
                boxes[I]=[]
            if board[i][j]!='.':
                if board[i][j] in (rows[i] or cols[j] or boxes[I]) or board[i][j] not in "123456789":
                    return "Invalid Sudoku Board"
                cols[j].append(board[i][j])
                rows[i].append(board[i][j])
                boxes[I].append(board[i][j])
    
    def isValid(row,col,val):
        if val in rows[row]:
            return False
        if val in cols[col]:
            return False
        R=int(row/3)*3
        C=int(col/3)
        if val in boxes[R+C]:
            return False
        rows[row].append(val)
        cols[col].append(val)
        boxes[R+C].append(val)
        return True
    
    def Remove(r,c,val):
        R=int(r/3)*3
        C=int(c/3)
        if val in rows[r]:
            rows[r].remove(val)
        if val in cols[c]:
            cols[c].remove(val)
        if val in boxes[R+C]:
            boxes[R+C].remove(val)
    
    def BackTrack(r,c):
        if r==len(board) or c==len(board[0]):
            return True
        else:
            if board[r][c]=='.':
                for val in range(1,10):
                    board[r][c]=str(val)
                    if isValid(r,c,str(val)):
                        if c==len(board[0])-1:
                            if BackTrack(r+1,0):
                                return True
                        else:
                            if BackTrack(r,c+1):
                                return True
                        Remove(r,c,str(val))
                    board[r][c]='.'
            else: 
                if c==len(board[0])-1:
                    if BackTrack(r+1,0):
                        return True
                else:
                    if BackTrack(r,c+1):
                        return True
    
    res=BackTrack(0,0)
    for i in board:
        print(i)
    return res
    # for i,j in boxes.items():
    #     print(f"{i}:{j}")


                 
                     
# print(solveSudoku([["5","3",".",".","7",".",".",".","."],
#                    ["6",".",".","1","9","5",".",".","."],
#                    [".","9","8",".",".",".",".","6","."],
#                    ["8",".",".",".","6",".",".",".","3"],
#                    ["4",".",".","8",".","3",".",".","1"],
#                    ["7",".",".",".","2",".",".",".","6"],
#                    [".","6",".",".",".",".","2","8","."],
#                    [".",".",".","4","1","9",".",".","5"],
#                    [".",".",".",".","8",".",".","7","9"]]))


# print(solveSudoku([[".",".","9","7","4","8",".",".","."],
#                    ["7",".",".",".",".",".",".",".","."],
#                    [".","2",".","1",".","9",".",".","."],
#                    [".",".","7",".",".",".","2","4","."],
#                    [".","6","4",".","1",".","5","9","."],
#                    [".","9","8",".",".",".","3",".","."],
#                    [".",".",".","8",".","3",".","2","."],
#                    [".",".",".",".",".",".",".",".","6"],
#                    [".",".",".","2","7","5","9",".","."]]))
print(solveSudoku([["1",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".",".","."]]))