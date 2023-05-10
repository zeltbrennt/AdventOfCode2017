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
        
if __name__ == '__main__':
    unittest.main()