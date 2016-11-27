import unittest

from vectors.PVector import PVector


class TestPVector(unittest.TestCase):
    def test_AddVectors(self):
        self.assertEqual(PVector(2, 2) + PVector(1, 1), PVector(3, 3))

    def test_iterator(self):
        self.assertEqual(tuple(PVector(2, 1)), (2, 1))

    def test_subtract_vector(self):
        self.assertEqual(PVector(5, 2) - PVector(3, 4), PVector(2, -2))



if __name__ == '__main__':
    unittest.main()
