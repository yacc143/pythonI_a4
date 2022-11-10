import unittest
import ex3


class TestEx3(unittest.TestCase):
    def test_split_result_empty(self):
        self.assertEqual(ex3.create_train_test_splits([], 0.5), ([], []))
    def test_split_half(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.5), ([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]))
    def test_split_twothirds(self):
        self.assertEqual(ex3.create_train_test_splits(list(range(10)), 0.67), ([0, 1, 2, 3, 4, 5], [6, 7, 8, 9]))
        
if __name__ == '__main__':
    unittest.main()