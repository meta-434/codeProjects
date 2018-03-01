import unittest
import eulerThree

class TestEulerThree(unittest.TestCase):

    def test_gpfFinder(self):
        result = eulerThree.gpfFinder(600851475143)
        self.assertEqual(result, 6857)

        lowest = eulerThree.gpfFinder(2)
        self.assertEqual(lowest, 2)

        with self.assertRaises(SystemExit): eulerThree.gpfFinder(0)

        absChecker = eulerThree.gpfFinder(-21)
        self.assertEqual(absChecker, 7)


if __name__ == "__main__":
    unittest.main(verbosity = 0, buffer = True)
