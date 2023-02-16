def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(list[start:end+1]))
        # This prints the remaining list and amount of steps taken each time we discard a list

        steps = steps + 1
        # Splitting the data into half
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 4, 7, 12, 44, 1, 9, 11]
target = 5

binary_search(my_list, target)
