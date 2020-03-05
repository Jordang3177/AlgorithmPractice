from unittest import TestCase
from Leetcode.Python.Finished.Easy.SameTree import Tree as Tree

from Leetcode.Python.Finished.Easy.countAndSay import Solution as CountSolution
from Leetcode.Python.Finished.Easy.AddBinary import Solution as BinarySolution
from Leetcode.Python.Finished.Easy.atoi import Solution as AtoiSolution
from Leetcode.Python.Finished.Easy.CheckIfExist import Solution as CIESolution
from Leetcode.Python.Finished.Easy.ClimbingStairs import Solution as ClimbingSolution
from Leetcode.Python.Finished.Easy.DefangIP import Solution as DefangSolution
from Leetcode.Python.Finished.Easy.Fib import Solution as FibSolution
from Leetcode.Python.Finished.Easy.IntegerToRoman import Solution as ITRSolution
from Leetcode.Python.Finished.Easy.IsAnagram import Solution as AnagramSolution
from Leetcode.Python.Finished.Easy.reverse_words import Solution as RWSolution
from Leetcode.Python.Finished.Easy.FizzBuzz import Solution as FBSolution
from Leetcode.Python.Finished.Easy.SameTree import Solution as TreeSolution
from Leetcode.Python.Finished.Easy.SymmetricTree import Solution as SymmetricSolution
from Leetcode.Python.Finished.Easy.max_depth import Solution as DepthSolution
from Leetcode.Python.Finished.Easy.min_depth import Solution as MinDepthSolution
from Leetcode.Python.Finished.Easy.PathSum import Solution as PathSumSolution
from Leetcode.Python.Finished.Easy.isPalindrome import Solution as NumPalindromeSolution
from Leetcode.Python.Finished.Easy.RemoveElements import Solution as RemoveElementsArraySolution


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


    def test_check_if_exist(self):
        S = CIESolution()
        self.assertEqual(S.checkIfExist([10,2,5,3]), True)
        self.assertEqual(S.checkIfExist([1]), False)
        self.assertEqual(S.checkIfExist([]), False)
        self.assertEqual(S.checkIfExist([1,1]), False)
        self.assertEqual(S.checkIfExist([1,3,5]), False)

    def test_climbing_stairs(self):
        S = ClimbingSolution()
        self.assertEqual(S.climbStairs(0), 1)
        self.assertEqual(S.climbStairs(1), 1)
        self.assertEqual(S.climbStairs(2), 2)
        self.assertEqual(S.climbStairs(3), 3)
        self.assertEqual(S.climbStairs(4), 5)
        self.assertEqual(S.climbStairs(5), 8)
        self.assertEqual(S.climbStairs(6), 13)
        self.assertEqual(S.climbStairs(7), 21)
        self.assertEqual(S.climbStairs(8), 34)
        self.assertEqual(S.climbStairs(9), 55)
        self.assertEqual(S.climbStairs(10), 89)

    def test_defang_ip(self):
        S = DefangSolution()
        self.assertEqual(S.defang_ip('1.1.1.1'), '1[.]1[.]1[.]1')
        self.assertEqual(S.defang_ip('250.0.168.1'), '250[.]0[.]168[.]1')
        self.assertEqual(S.defang_ip('168.1.1.0'), '168[.]1[.]1[.]0')

    def test_fib(self):
        S = FibSolution()
        self.assertEqual(S.fib(0), 0)
        self.assertEqual(S.fib(1), 1)
        self.assertEqual(S.fib(2), 1)
        self.assertEqual(S.fib(3), 2)
        self.assertEqual(S.fib(4), 3)
        self.assertEqual(S.fib(5), 5)
        self.assertEqual(S.fib(6), 8)
        self.assertEqual(S.fib(7), 13)
        self.assertEqual(S.fib(8), 21)
        self.assertEqual(S.fib(9), 34)
        self.assertEqual(S.fib(10), 55)
        self.assertEqual(S.fib(11), 89)
        self.assertEqual(S.fib(300), 222232244629420445529739893461909967206666939096499764990979600)

    def test_int_to_rom(self):
        S = ITRSolution()
        self.assertEqual(S.intToRoman(1), 'I')
        self.assertEqual(S.intToRoman(4), 'IV')
        self.assertEqual(S.intToRoman(1990), 'MCMXC')
        self.assertEqual(S.intToRoman(3999), 'MMMCMXCIX')
        self.assertEqual(S.intToRoman(90), 'XC')
        self.assertEqual(S.intToRoman(500), 'D')
        self.assertEqual(S.intToRoman(400), 'CD')
        self.assertEqual(S.intToRoman(100), 'C')
        self.assertEqual(S.intToRoman(50), 'L')
        self.assertEqual(S.intToRoman(40), 'XL')
        self.assertEqual(S.intToRoman(10), 'X')
        self.assertEqual(S.intToRoman(5), 'V')

    def test_is_anagram(self):
        S = AnagramSolution()
        self.assertEqual(S.isAnagram('anagram', 'nagaram'), True)
        self.assertEqual(S.isAnagram('rat', 'car'), False)
        self.assertEqual(S.isAnagram('too', 'oto'), True)
        self.assertEqual(S.isAnagram('wellthen', 'hi'), False)

    def test_reverse_words(self):
        S = RWSolution()
        self.assertEqual(S.reverse_words("let's get this started"), "s'tel teg siht detrats")
        self.assertEqual(S.reverse_words("how about now"), 'woh tuoba won')
        self.assertEqual(S.reverse_words("Well then"), "lleW neht")
        self.assertEqual(S.reverse_words("Come to me please"), "emoC ot em esaelp")

    def test_fizz_buzz(self):
        S = FBSolution()
        self.assertEqual(S.fizzBuzz(1), ['1'])
        self.assertEqual(S.fizzBuzz(2), ['1', '2'])
        self.assertEqual(S.fizzBuzz(3), ['1', '2', 'Fizz'])
        self.assertEqual(S.fizzBuzz(4), ['1', '2', 'Fizz', '4'])
        self.assertEqual(S.fizzBuzz(5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(S.fizzBuzz(6), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz'])
        self.assertEqual(S.fizzBuzz(7), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7'])
        self.assertEqual(S.fizzBuzz(8), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8'])
        self.assertEqual(S.fizzBuzz(9), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz'])
        self.assertEqual(S.fizzBuzz(10), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'])
        self.assertEqual(S.fizzBuzz(11), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11'])
        self.assertEqual(S.fizzBuzz(12), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz'])
        self.assertEqual(S.fizzBuzz(13), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13'])
        self.assertEqual(S.fizzBuzz(14), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14'])
        self.assertEqual(S.fizzBuzz(15), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])

    def test_same_tree(self):
        S = TreeSolution()
        tree1 = Tree()
        tree1.val = 1
        tree1.left = Tree()
        tree1.left.data = 2
        tree1.right = Tree()
        tree1.right.data = 3

        tree2 = Tree()
        tree2.val = 1
        tree2.left = Tree()
        tree2.left.data = 2
        tree2.right = Tree()
        tree2.right.data = 3

        self.assertEqual(S.same_tree(tree1, tree2), True)

        tree2.left.left = Tree()
        tree2.left.left.val = 4

        self.assertEqual(S.same_tree(tree1, tree2), False)

        tree2.left.left = None

        self.assertEqual(S.same_tree(tree1, tree2), True)

    def test_symmetric_tree(self):
        S = SymmetricSolution()
        self.assertEqual(S.isSymmetric(None), True)

        tree1 = Tree()
        tree1.val = 1
        self.assertEqual(S.isSymmetric(tree1), True)
        tree1.left = Tree()
        tree1.left.val = 2
        self.assertEqual(S.isSymmetric(tree1), False)
        tree1.right = Tree()
        tree1.right.val = 2
        self.assertEqual(S.isSymmetric(tree1), True)

    def test_max_depth(self):
        S = DepthSolution()
        self.assertEqual(S.maxDepth(None), 0)
        tree1 = Tree()
        tree1.val = 1
        self.assertEqual(S.maxDepth(tree1), 1)
        tree1.left = Tree()
        tree1.left.val = 3
        self.assertEqual(S.maxDepth(tree1), 2)
        tree1.left.left = Tree()
        tree1.left.left.val = 5
        self.assertEqual(S.maxDepth(tree1), 3)
        tree1.left.left.left = Tree()
        tree1.left.left.left.val = 4
        tree1.left.left.left.left = Tree()
        tree1.left.left.left.left.val = 7
        self.assertEqual(S.maxDepth(tree1), 5)

    def test_min_depth(self):
        S = MinDepthSolution()
        self.assertEqual(S.minDepth(None), 0)
        tree1 = Tree()
        tree1.val = 1
        self.assertEqual(S.minDepth(tree1), 1)
        tree1.left = Tree()
        tree1.left.val = 2
        self.assertEqual(S.minDepth(tree1), 2)
        tree1.right = Tree()
        tree1.right.val = 3
        tree1.right.left = Tree()
        tree1.right.left.val = 4
        tree1.right.right = Tree()
        tree1.right.right.val = 5
        self.assertEqual(S.minDepth(tree1), 2)

    def test_path_sum(self):
        S = PathSumSolution()
        self.assertEqual(S.hasPathSum(None, 0), False)
        tree1 = Tree()
        tree1.val = 5
        self.assertEqual(S.hasPathSum(tree1, 5), True)
        self.assertEqual(S.hasPathSum(tree1, 3), False)
        tree1.left = Tree()
        tree1.left.val = 4
        tree1.right = Tree()
        tree1.right.val = 8
        self.assertEqual(S.hasPathSum(tree1, 9), True)
        self.assertEqual(S.hasPathSum(tree1, 13), True)
        self.assertEqual(S.hasPathSum(tree1, 5), False)
        tree1.left.left = Tree()
        tree1.left.left.val = 11
        tree1.left.left.left = Tree()
        tree1.left.left.left.val = 7
        tree1.left.left.right = Tree()
        tree1.left.left.right.val = 2
        self.assertEqual(S.hasPathSum(tree1, 22), True)
        self.assertEqual(S.hasPathSum(tree1, 27), True)
        self.assertEqual(S.hasPathSum(tree1, 13), True)
        self.assertEqual(S.hasPathSum(tree1, 9), False)
        tree1.right.left = Tree()
        tree1.right.left.val = 13
        tree1.right.right = Tree()
        tree1.right.right.val = 4
        tree1.right.right.right = Tree()
        tree1.right.right.right.val = 1
        self.assertEqual(S.hasPathSum(tree1, 22), True)
        self.assertEqual(S.hasPathSum(tree1, 27), True)
        self.assertEqual(S.hasPathSum(tree1, 26), True)
        self.assertEqual(S.hasPathSum(tree1, 18), True)
        self.assertEqual(S.hasPathSum(tree1, 13), False)

    def test_ispalindrome(self):
        S = NumPalindromeSolution()
        self.assertEqual(S.isPalindrome(121), True)
        self.assertEqual(S.isPalindrome(-121), False)
        self.assertEqual(S.isPalindrome(0), True)
        self.assertEqual(S.isPalindrome(11), True)
        self.assertEqual(S.isPalindrome(1234321), True)
        self.assertEqual(S.isPalindrome(191), True)
        self.assertEqual(S.isPalindrome(144441), True)
        self.assertEqual(S.isPalindrome(-1), False)
        self.assertEqual(S.isPalindrome(12345678), False)
        self.assertEqual(S.isPalindrome(59678), False)

    def test_remove_elements(self):
        S = RemoveElementsArraySolution()
        self.assertEqual(S.removeElement([1,2,3,4,5], 1), 4)
        self.assertEqual(S.removeElement([1,1,1,1,1,1,1], 1), 0)
        self.assertEqual(S.removeElement([1,1,1,1,1,1,1,1,1,1,1],1), 0)
        self.assertEqual(S.removeElement([1,2,3,4,5,6,7,8], 10), 8)
        self.assertEqual(S.removeElement([1,2,3,4,5,6,7,8,9,10], 10), 9)
        self.assertEqual(S.removeElement([1], 1), 0)
        self.assertEqual(S.removeElement([1,2,3,4], 2), 3)