from turtle import *

BLOCK_SIZE = 5
GRID_TOP_LEFT_CORNER = (-400, 400)


def get_image_data_from_file(file):
    data = []

    for x in open(file, encoding="utf-8"):
        data.append(x.strip().split(4 * " "))

    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] = tuple(map(int, data[y][x].split(",")))

    return data


def to_pixels(x, y):
    x0, y0 = GRID_TOP_LEFT_CORNER
    return x0 + BLOCK_SIZE * x, y0 + BLOCK_SIZE * y


def square(x, y, colour):
    penup()
    colour(colour)
    goto(to_pixels(x,y))
    pendown()
    begin_fill()
    for _ in range(4):
        forward(BLOCK_SIZE)
        right(90)
    end_fill()


tracer(0, 1)
colormode(255)

data = get_image_data_from_file("image_data_1.txt")
for y in range(len(data)):
    for x in range(len(data[y])):
        square(x,y,data[x][y])


update()
exitonclick()
