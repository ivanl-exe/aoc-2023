from day import Day
from collections import defaultdict

def record_parser(record: str) -> dict:
    i = record.index(':')
    _id = int(record[len('Game '):i])
    grabs = [grab.split(', ') for grab in record[i+2:].split('; ')]
    marbles = {'id': _id, 'marbles': defaultdict(list)}
    for grab in grabs:
        for marble in grab:
            n, colour = marble.split()
            marbles['marbles'][colour].append(int(n))
    return marbles

def solution_one(data) -> int:
    s = 0
    for game in data:
        _id = game['id']
        marbles = game['marbles']
        red_marbles = marbles['red']
        green_marbles = marbles['green']
        blue_marbles = marbles['blue']
        #compare
        if max(red_marbles) > 12 or \
           max(green_marbles) > 13 or \
           max(blue_marbles) > 14:
            continue
        s += _id
    return s

def solution_two(data) -> int:
    s = 0
    for game in data:
        _id = game['id']
        marbles = game['marbles']
        red_marbles = marbles['red']
        green_marbles = marbles['green']
        blue_marbles = marbles['blue']
        #compare
        s += max(red_marbles) * \
             max(green_marbles) * \
             max(blue_marbles)
    return s

if __name__ == '__main__':
    day = Day(2, record_parser)
    result_one = day.solve(solution_one)
    print(result_one)
    result_two = day.solve(solution_two)
    print(result_two)