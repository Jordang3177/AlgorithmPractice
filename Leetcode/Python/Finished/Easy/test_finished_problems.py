from unittest import TestCase

from Leetcode.Python.Finished.Easy.countAndSay import Solution as CountSolution
from Leetcode.Python.Finished.Easy.AddBinary import Solution as BinarySolution
from Leetcode.Python.Finished.Easy.atoi import Solution as AtoiSolution


class TestSolution(TestCase):
    def test_count_and_say(self):
        S = CountSolution()
        self.assertEqual(S.countAndSay(1), '1')
        self.assertEqual(S.countAndSay(2), '11')
        self.assertEqual(S.countAndSay(3), '21')
        self.assertEqual(S.countAndSay(4), '1211')
        self.assertEqual(S.countAndSay(5), '111221')
        self.assertEqual(S.countAndSay(6), '312211')
        self.assertEqual(S.countAndSay(7), '13112221')

    def test_add_binary(self):
        S = BinarySolution()
        self.assertEqual(S.addBinary('0', '0'), '0')
        self.assertEqual(S.addBinary('11', '1'), '100')
        self.assertEqual(S.addBinary('1010', '1011'), '10101')
        self.assertEqual(S.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101","110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"), "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000")
        self.assertEqual(S.convertToBinary(1), '1')
        self.assertEqual(S.convertToBinary(0), '0')
        self.assertEqual(S.convertToBinary(10), '1010')

    def test_atoi(self):
        S = AtoiSolution()
        self.assertEqual(S.myAtoi('42'), 42)
        self.assertEqual(S.myAtoi('3439'), 3439)
        self.assertEqual(S.myAtoi('-13'), -13)
        self.assertEqual(S.myAtoi("     -42"), -42)
        self.assertEqual(S.myAtoi("         wow a 123"), 0)
        self.assertEqual(S.myAtoi("-234334853434325262343262362362362363"), -2**31)
        self.assertEqual(S.myAtoi("3248308420394637426384762347628346823"), 2**31 -1)
        self.assertEqual(S.myAtoi('-1+'), -1)
        self.assertEqual(S.myAtoi('+-2'), 0)
        self.assertEqual(S.myAtoi('-+2'), 0)
        self.assertEqual(S.myAtoi('000000'), 0)
        self.assertEqual(S.myAtoi('          0000            '), 0)
        self.assertEqual(S.myAtoi('0-1'), 0)
        self.assertEqual(S.myAtoi('           0-1'), 0)
        self.assertEqual(S.myAtoi('0+1'), 0)
        self.assertEqual(S.myAtoi('              0+1'), 0)
