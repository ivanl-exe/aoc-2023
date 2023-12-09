from day import Day
import re
from collections import defaultdict

SEQUENCE_PATTERN = '((?:\d+\s*)+)'
RECORD_PATTERN = re.compile(f'^Card\s+(\d+):\s+{SEQUENCE_PATTERN}\|\s+{SEQUENCE_PATTERN}')

def record_parser(record: str) -> dict:
    matches = re.search(RECORD_PATTERN, record)
    if not matches: return {}
    groups = matches.groups()
    #attributes
    card_id = int(groups[0])
    card_numbers, winning_numbers = [tuple(map(lambda n: int(n), group.split())) for group in groups[1:]]
    return {
        'id': card_id,
        'numbers': {
            'card': card_numbers,
            'winning': winning_numbers
        }
    }

def solution_one(data) -> int:
    s = 0
    for card in data:
        __numbers__ = card['numbers']
        card_numbers = __numbers__['card']
        winning_numbers = __numbers__['winning']
        t = [number in winning_numbers for number in card_numbers].count(True)
        n = 2 ** (t - 1) if t >= 1 else 0
        s += n
    return s

def solution_two(data) -> int:
    deck = defaultdict(int)
    height = len(data)
    for card in data:
        card_id = card['id']
        __numbers__ = card['numbers']
        card_numbers = __numbers__['card']
        winning_numbers = __numbers__['winning']
        deck[card_id] += 1
        mul = deck[card_id]
        #sequence
        card_id += 1
        t = [number in winning_numbers for number in card_numbers].count(True)
        sequence_numbers = tuple(range(card_id, min(card_id + t, height + 1)))
        for card_number in sequence_numbers:
            deck[card_number] += mul
    s = sum(deck.values())
    return s

if __name__ == '__main__':
    day = Day(4, record_parser)
    result_one = day.solve(solution_one)
    print(result_one)
    result_two = day.solve(solution_two)
    print(result_two)