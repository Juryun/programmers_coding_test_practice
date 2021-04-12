def solution(numbers):
    checklist = [0 for i in range(201)]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            add = numbers[i] + numbers[j]
            checklist[add] = checklist[add] + 1
    answer = []
    for i in range(len(checklist)):
        if checklist[i] != 0:
            answer.append(i)

    return answer