bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_max = [0]* bridge_length
    
    while bridge_max :
        answer += 1
        bridge_max.pop(0)
        # bridge_max.delete(0)
        
        if truck_weights:
            if sum(bridge_max)+truck_weights[0] <= weight:
                bridge_max.append(truck_weights.pop(0))
            else :
                bridge_max.append(0)
                
    return answer

solution(bridge_length, weight, truck_weights)