def solution(board,k):
    value=0
    for i in range(len(board)):
        n_board=list(map(int,board[i]))
        for j in range(len(n_board)):
            if i+j<=int(k): value=value+board[i][j]
            else: value=value
    return value

k=int(input('입력 by n:'))
board=[]
while input('계속 넣을거면 O입력')=='O':
    interval_new=list(input('newlist입력').split())
    board.append(interval_new)
