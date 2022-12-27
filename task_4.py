def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a,b):
    board = []
    board.append(a * ["X"])
    for _ in range(b-2):
        board.append(["X"] + (a -2) * ['.'] + ["X"])
    if b > 1:
     board.append(a * ["X"])
    return board
