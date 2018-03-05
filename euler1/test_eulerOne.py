import unittest
import eulerOne

class TestEulerOne(unittest.TestCase):

    def test_main(self):

        result = eulerOne.main()
        self.assertEqual(result, 233168)

if __name__ == "__main__":
    unittest.main()
