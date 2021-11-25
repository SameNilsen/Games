def binary_search(numbers, element):
    half = numbers[int(len(numbers)/2)]
    if len(numbers) == 1:
        return -float('inf')
    if half == element:
        return int(len(numbers)/2)
    elif half < element:
        return int(len(numbers)/2) + binary_search(numbers[int(len(numbers)/2):], element)
    elif half > element:
        return binary_search(numbers[:int(len(numbers)/2)], element)

print(binary_search([1, 4, 5, 7, 8, 9, 11, 14, 16, 19, 25], 12))