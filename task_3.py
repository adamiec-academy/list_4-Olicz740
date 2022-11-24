def min_max(data):
    min = 1
    max = 0
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    for i in range(len(data)):
        if data[i] <= max and data[i] < min:
            min = data[i]

    return min, max
