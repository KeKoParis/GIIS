import math

from lines.Bresenham import Bresenham


def Wu(event_1, event_2):
    x = event_1.x
    y = event_1.y

    dx = abs(event_2.x - event_1.x)
    dy = abs(event_2.y - event_1.y)

    points = []

    s1 = 1 if event_2.x > event_1.x else -1
    s2 = 1 if event_2.y > event_1.y else -1

    if dy > dx:
        dx, dy = dy, dx
        change_flag = True
    else:
        change_flag = False

    e = 2 * dy - dx

    for _ in range(dx + 1):
        points.append((x, y))
        while e >= 0:
            if change_flag:
                x += s1
            else:
                y += s2
            e -= 2 * dx
        if change_flag:
            y += s2
        else:
            x += s1
        e += 2 * dy

    k = (event_2.y - event_1.y) / (event_2.x - event_1.x)
    b = event_2.y - k * event_2.x
    additional = []
    if abs(event_2.y - event_1.y) < abs(event_2.x - event_1.x):
        for i in points:
            curr_y = i[0] * k + b
            additional.append((i[0], math.ceil(curr_y), 1 - abs(curr_y - i[1])))
    else:
        for i in points:
            curr_x = (i[1] - b) / k
            additional.append((math.ceil(curr_x), i[1], min((curr_x / i[0]), 1 - abs(curr_x - i[0]))))

    return points, additional
