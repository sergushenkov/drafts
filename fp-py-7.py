def add_points(points, n, m):
    new_points = set()
    for point in points:
        new_points.add((point[0] - 1, point[1]))
        new_points.add((point[0] + 1, point[1]))
        new_points.add((point[0], point[1] - 1))
        new_points.add((point[0], point[1] + 1))
    points = points | set(
        filter(lambda x: x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < m, new_points)
    )
    return points


def turn(points, n, m, day):
    if len(points) == n * m:
        return day
    else:
        return turn(add_points(points, n, m), n, m, day + 1)


def ConquestCampaign(n, m, l, points):
    day = 1
    all_points = n * m
    points = set(zip((x - 1 for x in battalion[::2]), (y - 1 for y in battalion[1::2])))
    return turn(points, n, m, day)


if __name__ == "__main__":
    n = 3
    m = 4
    l = 2
    battalion = [2, 2, 3, 4]
    print(ConquestCampaign(n, m, l, battalion))
