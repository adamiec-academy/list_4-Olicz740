def min_max(data):
    min = 0
    max = 0
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    for i in range(len(data)):
        if data[i] < max:
            min = data[i]

    return min , max
