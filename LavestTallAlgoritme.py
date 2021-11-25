def find_smallest_element(numbers):
    if len(numbers) == 1:
        print(numbers[0])
    else:
        if numbers[0] < numbers[1]:
            numbers.pop(1)
            find_smallest_element(numbers)
        else:
            numbers.pop(0)
            find_smallest_element(numbers)

find_smallest_element([3, 2, 1, 6, 4, 7, 5, 4, -9, 234, 2, -5])