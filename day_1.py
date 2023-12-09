from day import Day

#inefficient, but easy
def solution_one(data) -> int:
    s = 0
    for row in data:
        i = 0
        a, b = None, None
        while i < len(row):
            if a == None:
                a_temp = row[i]
                if a_temp.isnumeric(): a = a_temp
            if b == None:
                b_temp = row[-1-i]
                if b_temp.isnumeric(): b = b_temp
            i += 1
        s += int(a + b)
    return s

digits = {
    'one': '1', 
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

#pretty optimal
def solution_two(data) -> int:
    s = 0
    for row in data:
        numbers = []
        queue = []
        i = 0
        for c in row:
            if c.isnumeric():
                numbers.append(c)
                queue = []
            else:
                i = 0
                while i < len(queue):
                    number, j = queue[i]
                    if number[j] != c:
                        queue.pop(i)
                        continue
                    j += 1
                    if j == len(number):
                        digit = digits[number]
                        numbers.append(digit)
                        queue = []
                        continue
                    queue[i] = [number, j]
                    i += 1
                queue.extend(
                    [[digit, 1] for digit in digits.keys() if digit[0] == c]
                )
        s += int(numbers[0] + numbers[-1])
    return s

if __name__ == '__main__':
    day = Day(1)
    result_one = day.solve(solution_one)
    print(result_one)
    result_two = day.solve(solution_two)
    print(result_two)