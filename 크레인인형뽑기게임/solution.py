def solution(board, moves):
    answer = 0
    stack=[]
    for i in range(len(moves)):
        move = moves[i]-1
        for j in range(len(board[0])):
            if board[j][move] !=0:
                    if len(stack)==0 :
                        stack.append(board[j][move])
                        board[j][move] = 0
                        break
                    if stack[-1] == board[j][move]:
                        stack.pop()
                        answer = answer +2
                    else :
                        stack.append(board[j][move])
                    board[j][move] = 0
                    break

    return answer