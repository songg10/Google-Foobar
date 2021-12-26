def solution(n):
    n = int(n)
    op_count = 0
    while n > 1:
        print(n)
        if n % 2 == 0:
            n /= 2
        else:
            # Edge case: n == 3
            # If n == 3, decrementing it will result 
            # in 2 which could not be divided by 4
            if (n - 1) % 4 == 0 or n == 3:
                n -= 1
            else:
                n += 1
        op_count += 1
        
    return op_count

# print(solution('15'))

# print(solution('4'))

print(solution('3'))