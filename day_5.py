from typing import Union
from day import Day
import re
from collections import defaultdict

RECORD_PATTERN = re.compile('^(\w+)(?:-to-(\w+)\smap)?:')

def record_parser(record: str) -> Union[dict, None]:
    if record.replace('', ' ') == '': return None
    colon = record.find(':')
    if colon != -1:
        map_attribute = re.search(RECORD_PATTERN, record).groups()
        global current_attribute
        current_attribute = map_attribute
    colon += 1
    if len(record) != (colon):
        map_values = tuple(map(int, record[colon:].split()))
        return {
            'attribute': current_attribute,
            'values': map_values
        }
    return None

class AtlasValues:
    def __init__(self, to: str, values: list[int]) -> None:
        self.to = to
        self.values = values

def explorer(data: dict) -> dict:
    atlas = defaultdict(dict)
    for map in data:
        __attribute__ = map['attribute']
        map_from, map_to = __attribute__
        map_values = map['values']
        #add
        if map_from not in atlas:
            values = AtlasValues(map_to, list(map_values))
            atlas[map_from].update(vars(values))
        else:
            atlas[map_from]['values'].append(map_values)
    return atlas

def solution_one(data) -> int:
    pass

def solution_two(data) -> int:
    pass

if __name__ == '__main__':
    day = Day(5, record_parser)
    day.update(explorer)
    result_one = day.solve(solution_one)
    print(result_one)
    result_two = day.solve(solution_two)
    print(result_two)