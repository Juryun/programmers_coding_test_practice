def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        for j in range(101):
            if progresses[i] + j*speeds[i] >=100:
                day.append(j)
                break
    answer = []
    max_day = 0
    count = 0
    for i in range(len(day)):
        d = day.pop(0)
        if d <= max_day:
            count = count +1
        elif d > max_day:
            if count!=0:
                answer.append(count)
            max_day = d
            count = 1
    answer.append(count)
    return answer