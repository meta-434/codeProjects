import unittest
import eulerFour

class TestEulerFour(unittest.TestCase):

    #def test_digits(self):
        #result = eulerThree.gpfFinder(600851475143)
        #self.assertEqual(result, 6857)
    #def test_reverse(self):
    def test_palindromic(self):
        given = int(eulerFour.palindromic())
        reverse = int(eulerFour.reverse(eulerFour.palindromic()))
        self.assertEqual(given, reverse)
if __name__ == "__main__":
    unittest.main()
