from typing import Callable

class Reader:
    def __init__(self, filepath: str, parser: Callable) -> None:
        self.filepath = filepath
        raw_data = None
        with open(self.filepath, 'r') as file:
            raw_data = file.read()
        self.raw_data = raw_data

        #parse
        self.data = parser(self.raw_data)