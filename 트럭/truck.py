# from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    
    # bridge = deque()
    # bridge_max = deque(truck_weights)
    
    
    for i in truck_weights:
        if len(bridge) == 0 or bridge[-1][0]+i > weight :
            bridge.append([i, 1])
            
        else :
            bridge[-1][0] += i
            bridge[-1][1] += 1
    
    
    return answer