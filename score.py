with open('points', 'r') as f:
    text = f.read()
    max_score, last_points = list(map(lambda x: int(x), text.split(', ')))


def new_points(points):
    global max_score, last_points
    if points > max_score:
        max_score = points
    last_points = points
    with open('points', 'w') as f:
        f.write(f'{max_score}, {last_points}')


def return_points():
    global max_score, last_points
    return max_score, last_points
