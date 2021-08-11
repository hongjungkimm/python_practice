for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    n = 1
    while n <= N:
        max_box_idx = 0
        for i in range(100):
            if boxes[i] > boxes[max_box_idx]:
                max_box_idx = i

        min_box_idx = 0
        for i in range(100):
            if boxes[min_box_idx] > boxes[i]:
                min_box_idx = i

        if boxes[max_box_idx] - boxes[min_box_idx] <= 1:
            break

        boxes[max_box_idx] -= 1
        boxes[min_box_idx] += 1

        n += 1

    for i in range(100):
        if boxes[i] > boxes[max_box_idx]:
            max_box_idx = i

    min_box_idx = 0
    for i in range(100):
        if boxes[min_box_idx] > boxes[i]:
            min_box_idx = i

    result = boxes[max_box_idx] - boxes[min_box_idx]
    print('#{0} {1}'.format(tc, result))