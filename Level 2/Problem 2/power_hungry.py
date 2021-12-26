def solution(xs):
    # Filtered positive, zeros, and negative into each list
    pos_panels = [x for x in xs if x > 0]
    neg_panels = [x for x in xs if x < 0]
    zeros = [x for x in xs if x == 0]

    # Edge case: When the whole array is 0
    if len(zeros) == len(xs):
        return '0'

    if len(neg_panels) % 2 != 0 and len(pos_panels) == 0 and len(zeros) > 0:
        return '0'

    # If the number of negative number is by factor of 2,
    # we can guarantee that the product will always be positive
    # Removing the negative value with smallest absolute value
    # Edge case: If the only element in the array is negative then
    # do not remove it.
    if len(neg_panels) % 2 != 0 and len(neg_panels) > 1:
        neg_panels.sort(reverse=True)
        neg_panels.pop(0)

    return str(product(pos_panels + neg_panels))


def product(lst):
    '''Calculating a product of a list (Assuming the list never empty)'''
    product = 1
    for i in lst:
        product *= i

    return product

print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([0]))
print(solution([-2]))
print(solution([0, 0, -4, 0]))