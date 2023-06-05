import functools

def part1(puzzle):
    result = knot_hash(list(range(256)), puzzle)[0]
    return result[0] * result[1]

def part2(puzzle):
    lengths = string_to_ASCII(puzzle)
    numbers = list(range(256))
    current = 0
    skip = 0
    for _ in range(64):
        numbers, current, skip = knot_hash(numbers, lengths, current, skip)
    dense_hash = dense(numbers)
    return repr_hex(dense_hash)

def knot_hash(numbers: list, lengths: list, current = 0, skip = 0) -> tuple:
    for length in lengths:
        if (current + length) <= len(numbers) :
            sublist = numbers[current:current+length]
            numbers = numbers[:current] + sublist[::-1] + numbers[current+length:]
        else:
            sublist_a = numbers[current:]
            pivot = length - len(sublist_a)
            sublist_b = numbers[:pivot]
            sublist = sublist_a + sublist_b
            sublist = sublist[::-1]
            sublist_a = sublist[:length - pivot]
            sublist_b = sublist[length - pivot:]
            numbers = sublist_b + numbers[len(sublist_b):current] + sublist_a
        current = (current + length + skip) % len(numbers)
        skip += 1
    return numbers, current, skip

def string_to_ASCII(str: str) -> list[int]:
    bytes = []
    for s in str:
        bytes.append(ord(s))
    return bytes + [17,31,73,47,23]

def dense(numbers: list) -> list[int]:
    hash = []
    for i in range(0, len(numbers), 16):
        sublist = numbers[i:i+16]
        hash.append(functools.reduce(lambda a, b: a ^ b, sublist, 0))
    return hash
        
def repr_hex(numbers: list[int]) -> str:
    return "".join([hex(n)[2:].zfill(2) for n in numbers])