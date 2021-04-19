def solution(priorities, location):
    count = 0
    answer = 0
    while True:
        p = priorities.pop(0)
        if len(priorities) == 0:
            answer = count+1
            break
        if p<max(priorities):
            priorities.append(p)
        elif p>=max(priorities) and location ==0:
            answer = count+1
            break
        elif p>=max(priorities) and location != 0:
            count = count +1
        location = location -1
        if location == -1:
            location = len(priorities)-1
    return answer