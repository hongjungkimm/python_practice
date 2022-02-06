def solution(priorities, location):

    order = list(range(len(priorities)))
    result = []
    result_order = []
    while priorities:
        max_num = max(priorities)
        if max_num == priorities[0]:
            result.append(priorities[0])
            result_order.append(order[0])
            priorities.pop(0)
            order.pop(0)
        else:
            priorities.append(priorities.pop(0))
            order.append(order.pop(0))
    
    for i in range(len(result_order)):
        if result_order[i] == location:
            return i + 1