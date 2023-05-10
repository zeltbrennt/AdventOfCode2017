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
        
if __name__ == '__main__':
    unittest.main()