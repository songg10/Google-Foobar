def solution(x, y):
    id =  ((x+y-1)*(x+y))/2 - y + 1
    return str(int(id))

print(solution(5,10))
print(solution(4,1))
print(solution(3,2))
