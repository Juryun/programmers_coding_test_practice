def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = []
    now = 0
    while True:
        if len(truck_weights) == 0:
            answer = answer + len(queue) + bridge_length
            break

        if len(queue)<bridge_length :
            if now + truck_weights[0] <= weight:
                now = now + truck_weights[0]
                queue.append(truck_weights.pop(0))
            elif now + truck_weights[0] > weight:
                queue.append(0)
        elif len(queue) == bridge_length :
            answer = answer +1
            now = now - queue.pop(0)
    return answer