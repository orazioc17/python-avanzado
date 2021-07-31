"""Testing the methods"""


import unittest
from unittest import TestCase
from palindrome import is_palindrome
from prime_number import is_prime
from division_closure import make_division_by


class TestingFunctions(TestCase):
    """Tests to know if the methods works well"""
    
    def test_is_palindrome(self):
        """Testing is_palindrome method"""
        self.assertEqual(is_palindrome('Ligar es ser agil'), True)
        self.assertEqual(is_palindrome('Arepera'), True)
        self.assertEqual(is_palindrome('Esto no es un palindromo'), False)
        self.assertEqual(is_palindrome('ESto tampoco es un palindromo'), False)
        self.assertEqual(is_palindrome('Ana'), True)

    def test_is_prime(self):
        """Testing is_prime method"""
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(200), False)
        self.assertEqual(is_prime(53), True)
        self.assertEqual(is_prime(23), True)
        self.assertEqual(is_prime(45), False)
        self.assertEqual(is_prime(32), False)
        self.assertEqual(is_prime(142), False)

    def test_make_division_by(self):
        division_by_3 = make_division_by(3)
        self.assertEqual(division_by_3(15), 5)
        division_by_3 = make_division_by(3)
        self.assertEqual(division_by_3(30), 10)
        division_by_3 = make_division_by(10)
        self.assertEqual(division_by_3(100), 10)
        division_by_3 = make_division_by(7)
        self.assertEqual(division_by_3(49), 7)


if __name__ == '__main__':
    unittest.main()