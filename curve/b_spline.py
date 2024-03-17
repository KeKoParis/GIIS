def b_spline(p0, p1, p2, p3, num_points=1000):
    points = []
    for i in range(num_points):
        t = i / (num_points - 1)
        t2 = t * t
        t3 = t2 * t
        mt = 1 - t
        mt2 = mt * mt
        mt3 = mt2 * mt

        x = mt3 * p0.x + 3 * mt2 * t * p3[0] + 3 * mt * t2 * p2[0] + t3 * p1.x
        y = mt3 * p0.y + 3 * mt2 * t *p3[1] + 3 * mt * t2 * p2[1] + t3 * p1.y

        points.append((x, y))
    return points
