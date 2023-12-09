from typing import Union
from day import Day
from collections import defaultdict

def is_neighbour(
        data,
        coordinate: tuple[int, int],
        resolution: tuple[int, int],
        conditional = lambda c: not(c == '.' or c.isnumeric())
    ) -> Union[tuple[int, int], bool]:
    width, height = resolution
    for di in range(-1, 2):
        for dj in range(-1, 2):
            i, j = coordinate
            i += di
            j += dj
            if i < 0 or i >= height or \
               j < 0 or j >= width:
                continue
            c = data[i][j]
            if conditional(c): yield (i, j)
    return False 

def solution_one(data) -> int:
    s = 0
    height = len(data)
    for i in range(height):         
        row = data[i]
        width = len(row)
        flag = False
        for j in range(width):
            c = row[j]
            if not c.isnumeric():
                if flag == True: s += int(n)
                n = ''
                flag = False
                continue
            n += c
            neighbourhood = is_neighbour(
                data,
                (i, j),
                (width, height)
            )
            #check
            if not neighbourhood: continue
            flag = True
    return s

def mul(l: list) -> Union[int, float]:
    p = 1
    for n in l: p *= n
    return p

def solution_two(data) -> int:
    d = defaultdict(list)
    height = len(data)
    for i in range(height):
        row = data[i]
        width = len(row)
        flag = False
        for j in range(width):
            c = row[j]
            #init & reset
            if j == 0 or not c.isnumeric():
                if flag == True:
                    [d[neighbour].append(int(n)) for neighbour in neighbours]
                    flag = False
                n = ''
                neighbours = []
                continue
            n += c
            #check
            neighbourhood = is_neighbour(
                data,
                (i, j),
                (width, height),
                conditional = lambda c: c == '*'
            )
            if neighbourhood == False: continue
            [neighbours.append(neighbour) for neighbour in neighbourhood if neighbour not in neighbours]
            flag = True
    s = sum([mul(l) for l in d.values() if len(l) > 1])
    return s

if __name__ == '__main__':
    day = Day(3)
    result_one = day.solve(solution_one)
    print(result_one)
    result_two = day.solve(solution_two)
    print(result_two)