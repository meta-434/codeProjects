import unittest
import eulerThree

class TestEulerThree(unittest.TestCase):

    def test_gpfFinder(self):
        result = eulerThree.gpfFinder(600851475143)
        self.assertEqual(result, 6857)

if __name__ == "__main__":
    unittest.main()
