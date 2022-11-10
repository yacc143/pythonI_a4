import unittest
import ex5


class TestEx5(unittest.TestCase):
    def test_ascending(self):
        some_list = [1, 3, 0, 4, 5]
        self.assertEqual(ex5.sort(some_list), None)
        self.assertEqual(some_list, [0, 1, 3, 4, 5])

    def test_descending(self):
        some_list = [1, 3, 0, 4, 5]
        self.assertEqual(ex5.sort(some_list, ascending=False), None)
        self.assertEqual(some_list, [5, 4, 3, 1, 0])

    
if __name__ == '__main__':
    unittest.main()