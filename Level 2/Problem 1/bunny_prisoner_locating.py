def solution(x, y):
    x_1 = y_1 = id = 1
    while x_1 < x or y_1 < y:
        y_1 = x_1
        x_1 = 1
        y_1 += 1
        id += 1

        while y_1 != 1:
            if x_1 == x and y_1 == y:
                break
            y_1 -= 1
            x_1 += 1
            id += 1

    return id

# print(solution(5,10))
# print(solution(4,1))


def quyen_solution(x, y):
    sum_t = x+y-1
    f = sum([k for k in range(sum_t+1)])

    return f-y+1

print(quyen_solution(2, 5))