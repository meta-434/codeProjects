import unittest
import eulerTwo

class TestEulerTwo(unittest.TestCase):

    def test_fibbFinder(self):

        result = eulerTwo.fibbFinder()
        self.assertEqual(result, 4613732)

if __name__ == "__main__":
    unittest.main()
