from collections import deque
def solution(queue1, queue2):
    answer = 0
    result = (sum(queue1)+sum(queue2))/2
    queue1, queue2 = deque(queue1), deque(queue2)
    for i in queue1 :
        if i > result :
            return -1
    for i in queue2 :
        if i > result :
            return -1
    if (sum(queue1)+sum(queue2)) %2 != 0 :
        return -1
    while True :
        if sum(queue1) == sum(queue2) :
            break
        elif sum(queue1) > sum(queue2) :
            queue2.append(queue1.popleft())
            answer += 1
        elif sum(queue1) < sum(queue2) :
            queue1.append(queue2.popleft())
            answer += 1
    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))