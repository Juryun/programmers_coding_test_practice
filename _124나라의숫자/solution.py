def solution(n):
    answer = ''
    arr = []
    size = 0
    sum1 = 0
    for i in range(1, 50000):
        cnt = pow(3,i)
        nowsum = sum1 + cnt
        if nowsum >= n:
            size = i
            break
        else :
            sum1 = nowsum
    if size == 1:
        if n == 3:
            answer = answer + '4'
            return answer
        elif n ==2:
            answer = answer + '2'
            return answer
        elif n ==1:
            answer = answer + '1'
            return answer
    new = n - sum1
    for i in range(size):
        if ((new-1) % pow(3,size - i)) >= pow(3,size - i-1) * 2:
            answer = answer + '4'
            new = new - pow(3,size - i-1)*2
        elif ((new-1) % pow(3,size - i)) >= pow(3,size - i-1):
            answer = answer + '2'
            new = new - pow(3,size - i-1)
        else:
            answer = answer + '1'
            new = new - 0


    return answer