def XOR_of_sequence(n):
    '''XOR from 1 to n'''
    if n <= 0:
        return 0

    r = n % 4
    if r == 0:
        return n
    elif r == 1:
        return 1
    elif r == 2:
        return n+1

    # If we have a remainder of 3
    return 0

def solution(start, length):
    # Process the xor of first 2 rows
    checksum = XOR_of_sequence(start + 2*(length-1))
    if start > 1:
        # If the start is not 1 nor 0, then discard the xor of sequence from start - 1
        checksum ^= XOR_of_sequence(start - 1)

    # Start at row 3 (if there is row 3)
    checksum_length = length - 2
    start += length*2
    while checksum_length > 0:
        checksum ^= XOR_of_sequence(start+checksum_length-1) ^ XOR_of_sequence(start-1)
        start += length
        checksum_length -= 1
    
    return checksum

# print(solution(0, 3))

# print(solution(17, 4))


print(XOR_of_sequence(16))

print(XOR_of_sequence(20))

print(16^20)
print(17^18^19^20)

# print(3^1^6)
# print(0^1^2)
# print(3^4)
# print(3^7^6)