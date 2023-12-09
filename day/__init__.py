from typing import Callable
from day.reader.custom.advent import AdventReader

class Day(AdventReader):
    def __init__(self, day: int, record_parser: Callable = None) -> None:
        self.day = day
        filepath = f'inputs/day_{day}.txt'
        super().__init__(filepath)
        if record_parser == None: return None
        i = 0
        while i < len(self.data):
            record = self.data[i]
            record = record_parser(record)
            if record == None:
                self.data.pop(i)
                continue
            self.data[i] = record
            i += 1
    
    def solve(self, solution: Callable):
        return solution(self.data)
    
    def update(self, updater: Callable) -> None:
        self.data = updater(self.data)