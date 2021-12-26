def solution(i):
    result = ''
    
    cur_number = 2
    
    while len(result) < 10005:
        if is_prime(cur_number):
            result += str(cur_number)
            
        cur_number += 1
        
    return result[i:i+5]
    
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
        

print(solution(0))

print(solution(3))