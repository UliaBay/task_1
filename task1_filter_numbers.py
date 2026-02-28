def filter_numbers(numbers, threshold = 0, greater = True):
    k = []
    if not numbers:
        return None
    if greater:
        for i in numbers:
            if i > threshold:
                k.append(i)
        return k
    else:
        for i in numbers:
            if i < threshold:
                k.append(i)
        return k
print(filter_numbers([1, -5, 10, 0, 3], threshold = 0, greater = True))
print(filter_numbers([1, -5, 10, 0, 3], threshold = 0, greater = False))
print(filter_numbers([], threshold = 5))
print(filter_numbers([1, 2, 3, 4, 5], threshold = 3, greater = True))
print(filter_numbers([1, 2, 3, 4, 5], threshold = 3, greater = False))

