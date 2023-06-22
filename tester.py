import unittest
from solutions import *

class Day01(unittest.TestCase):
    
    def test_part_1_example_1(self):
        self.assertEqual(day01.part1("1122"), 3)
    def test_part_1_example_2(self):
        self.assertEqual(day01.part1("1111"), 4)
    def test_part_1_example_3(self):
        self.assertEqual(day01.part1("1234"), 0)
    def test_part_1_example_4(self):
        self.assertEqual(day01.part1("91212129"), 9)
    def test_part_2_example_1(self):
        self.assertEqual(day01.part2("1212"), 6)
    def test_part_2_example_2(self):
        self.assertEqual(day01.part2("1221"), 0)
    def test_part_2_example_3(self):
        self.assertEqual(day01.part2("123425"), 4)   
    def test_part_2_example_4(self):
        self.assertEqual(day01.part2("123123"), 12)
    def test_part_2_example_5(self):
        self.assertEqual(day01.part2("12131415"), 4)
        
class Day02(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(day02.part1([[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]), 18)
    def test_part_2(self):
        self.assertEqual(day02.part2([[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]]), 9)
        
class Day03(unittest.TestCase):
    def test_part_1_example_1(self):
        self.assertEqual(day03.part1(1), 0)
    def test_part_1_example_2(self):
        self.assertEqual(day03.part1(12), 3)
    def test_part_1_example_3(self):
        self.assertEqual(day03.part1(23), 2)
    def test_part_1_example_4(self):
        self.assertEqual(day03.part1(1024), 31)
    def test_part_2_example_1(self):
        self.assertEqual(day03.part2(1), 2)
    def test_part_2_example_2(self):
        self.assertEqual(day03.part2(23), 25)
    def test_part_2_example_3(self):
        self.assertEqual(day03.part2(747), 806)
        
class Day04(unittest.TestCase):
    def test_part_1_example_1(self):
        self.assertEqual(day04.isValid("aa bb cc dd ee", 1), True)
    def test_part_1_example_2(self):
        self.assertEqual(day04.isValid("aa bb cc dd aa", 1), False)
    def test_part_1_example_3(self):
        self.assertEqual(day04.isValid("aa bb cc dd aaa", 1), True)
    def test_part_2_example_1(self):
        self.assertEqual(day04.isValid("abcde fghij", 2), True)
    def test_part_2_example_2(self):
        self.assertEqual(day04.isValid("abcde xyz ecdab", 2), False)
    def test_part_2_example_3(self):
        self.assertEqual(day04.isValid("iiii oiii ooii oooi oooo", 2), True)
    def test_part_2_example_4(self):
        self.assertEqual(day04.isValid("oiii ioii iioi iiio", 2), False)
        
class Day05(unittest.TestCase):
    def test_part1_full_example(self):
        self.assertEqual(day05.jump([0, 3, 0, 1, -3], False), (5, [2, 5, 0, 1, -2]))
    def test_part2_full_example(self):
        self.assertEqual(day05.jump([0, 3, 0, 1, -3], True), (10, [2, 3, 2, 3, -1]))
        
class Day06(unittest.TestCase):
    def test_part1_example1(self):
        bank = [0, 2, 7, 0]
        day06.balance(bank)
        self.assertEqual(bank, [2, 4, 1, 2])
    def test_part1_full_example(self):
        self.assertEqual(day06.part1([0,2, 7, 0]), 5)
    def test_part2_full_example(self):
        self.assertEqual(day06.part2([0, 2, 7, 0]), 4)
        
class Day07(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example = [
            "pbga (66)",
            "xhth (57)",
            "ebii (61)",
            "havc (66)",
            "ktlj (57)",
            "fwft (72) -> ktlj, cntj, xhth",
            "qoyq (66)",
            "padx (45) -> pbga, havc, qoyq",
            "tknk (41) -> ugml, padx, fwft",
            "jptl (61)",
            "ugml (68) -> gyxo, ebii, jptl",
            "gyxo (61)",
            "cntj (57)"
        ]
    def test_part1_example(self):
        self.assertEqual(day07.part1(self.example), "tknk")
        
    def test_part2_example(self):
        self.assertEqual(day07.part2(self.example), 60)
        
class Day08(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example = [
            "b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10"
]
    def test_part1_example(self):
        self.assertEqual(day08.part1(self.example), 1)
    def test_part2_example(self):
        self.assertEqual(day08.part2(self.example), 10)
    
class Day09(unittest.TestCase):
    def test_part1_example_1(self):
        self.assertEqual(day09.part1("{{{}}}"), 6)
    def test_part1_example_2(self):
        self.assertEqual(day09.part1("{{},{}}"), 5)
    def test_part1_example_3(self):
        self.assertEqual(day09.part1("{{{},{},{{}}}}"), 16)
    def test_part1_example_4(self):
        self.assertEqual(day09.part1("{<a>,<a>,<a>,<a>}"),1)
    def test_part1_example_5(self):
        self.assertEqual(day09.part1("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
    def test_part1_example_6(self):
        self.assertEqual(day09.part1("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
    def test_part1_example_7(self):
        self.assertEqual(day09.part1("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)
    def test_part2_example_1(self):
        self.assertEqual(day09.part2("<>"), 0)
    def test_part2_example_2(self):
        self.assertEqual(day09.part2("<random characters>"), 17)
    def test_part2_example_3(self):
        self.assertEqual(day09.part2("<<<<>"), 3)
    def test_part2_example_4(self):
        self.assertEqual(day09.part2("<{!>}>"),2)
    def test_part2_example_5(self):
        self.assertEqual(day09.part2("<!!>"), 0)
    def test_part2_example_6(self):
        self.assertEqual(day09.part2("<!!!>>"), 0)
    def test_part2_example_7(self):
        self.assertEqual(day09.part2('<{o"i!a,<{i<a>'), 10)   
        
class Day10(unittest.TestCase):
    def test_part1_example(self):
        result = day10.hash_iter(list(range(5)), [3, 4, 1, 5])[0]
        self.assertEqual(result[0] * result[1], 12)
    def test_ASCII_transform(self):
        self.assertEqual(day10.string_to_ASCII("1,2,3"), [49,44,50,44,51,17,31,73,47,23])
    def test_dense(self):
        self.assertEqual(day10.dense([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]), [64])
    def test_repr_hex(self):
        self.assertEqual(day10.repr_hex([64, 7, 255]), "4007ff")
    def test_part2_ex1(self):
        self.assertEqual(day10.part2(""), "a2582a3a0e66e6e86e3812dcb672a272")
    def test_part2_ex2(self):
        self.assertEqual(day10.part2("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
    def test_part2_ex3(self):
        self.assertEqual(day10.part2("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
    def test_part2_ex3(self):
        self.assertEqual(day10.part2("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")
        
class Day11(unittest.TestCase):
    def test_part1_ex1(self):
        self.assertEqual(day11.part1("ne,ne,ne"), 3)
    def test_part1_ex2(self):
        self.assertEqual(day11.part1("ne,ne,sw,sw"), 0)
    def test_part1_ex3(self):
        self.assertEqual(day11.part1("ne,ne,s,s"), 2)
    def test_part1_ex4(self):
        self.assertEqual(day11.part1("se,sw,se,sw,sw"), 3)

class Day12(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example = [
            "0 <-> 2",
            "1 <-> 1",
            "2 <-> 0, 3, 4",
            "3 <-> 2, 4",
            "4 <-> 2, 3, 6",
            "5 <-> 6",
            "6 <-> 4, 5",
        ]
    def test_input_parsing(self):
        self.assertEqual(day12.parse_input(self.example), {'0': ['2'], '1': ['1'], '2': ['0', '3', '4'], '3': ['2', '4'], '4': ['2', '3', '6'], '5': ['6'], '6': ['4', '5']})
    def test_part1(self):
        self.assertEqual(day12.part1(self.example), 6)
    def test_part2(self):
        self.assertEqual(day12.part2(self.example), 2)
        
class Day13(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example = ["0: 3", "1: 2", "4: 4", "6: 4"]
    def test_part1(self):
        self.assertEqual(day13.part1(self.example), 24)
    def test_part2(self):
        self.assertEqual(day13.part2(self.example), 10)
        
class Day14(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(day14.part1("flqrgnkx"), 8108)
    def test_neighbors1(self):
        self.assertEqual(day14.get_neighbors(0, 0), [(1, 0), (0, 1)])
    def test_part2(self):
        self.assertEqual(day14.part2("flqrgnkx"), 1242)
        
class Day15(unittest.TestCase):
    def test_generator_1(self):
        self.assertEqual(day15.generate(65, 16807, 1),1092455)
    def test_generator_2(self):
        self.assertEqual(day15.generate(8921, 48271, 1),430625591)
    def test_part1_example(self):
        self.assertEqual(day15.part1((65, 8921)), 588)
    def test_part2_example(self):
        self.assertEqual(day15.part2((65, 8921)), 309)
        
class Day16(unittest.TestCase):
    def test_part1_example1(self):
        self.assertEqual(day16.spin(list("abcde"), 1), list("eabcd"))
    def test_part1_example2(self):
        self.assertEqual(day16.exchange(list("eabcd"), 3, 4), list("eabdc"))
    def test_part1_example3(self):
        self.assertEqual(day16.partner(list("eabdc"), "e", "b"), list("baedc"))
        
class Day17(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(day17.part1(3), 638)
        
class Day18(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example1 = [
            "set a 1",
            "add a 2",
            "mul a a",
            "mod a 5",
            "snd a",
            "set a 0",
            "rcv a",
            "jgz a -1",
            "set a 1",
            "jgz a -2"
        ]
        self.example2 = [
            "snd 1",
            "snd 2",
            "snd p",
            "rcv a",
            "rcv b",
            "rcv c",
            "rcv d"
        ]
    def test_part1(self):
        self.assertEqual(day18.part1(self.example1), 4)
    def test_part2(self):
        self.assertEqual(day18.part2(self.example2), 3)
        
class Day19(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.example = [
            "     |          ",
            "     |  +--+    ",
            "     A  |  C    ",
            " F---|----E|--+ ",
            "     |  |  |  D ",
            "     +B-+  +--+ "
        ]
    def test_part1_example(self):
        self.assertEqual(day19.part1(self.example), "ABCDEF")
    def test_part2_example(self):
        self.assertEqual(day19.part2(self.example), 38)
        
if __name__ == '__main__':
    unittest.main()