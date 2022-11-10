# as builtins.round is not allowed to be used for the implementation, fix it up here:
import builtins
builtin_round = builtins.round
def failing_round(*args, **kw):
    raise AssertionError("buildins.round is forbidden")
builtins.round = failing_round

import unittest
import ex4
import random


class TestEx4(unittest.TestCase):
    def test_round_nd_None(self):
        self.assertEqual(ex4.round_(777.777, None), 778)

    def test_round_nd_0(self):
        self.assertEqual(ex4.round_(777.777, 0), 778.0)


    def test_round_nd_1(self):
        self.assertEqual(ex4.round_(777.777, 1), 777.8)


    def test_round_nd_2(self):
        self.assertEqual(ex4.round_(777.777, 2), 777.78)


    def test_round_nd_3(self):
        self.assertEqual(ex4.round_(777.777, 3), 777.777)


    def test_round_nd_4(self):
        self.assertEqual(ex4.round_(777.777, 4), 777.777)


    def test_round_nd_m1(self):
        self.assertEqual(ex4.round_(777.777, -1), 780.0)


    def test_round_nd_m2(self):
        self.assertEqual(ex4.round_(777.777, -2), 800.0)


    def test_round_nd_m3(self):
        self.assertEqual(ex4.round_(777.777, -3), 1000.0)


    def test_round_nd_m4(self):
        self.assertEqual(ex4.round_(777.777, -4), 0.0)


class TestEx4Haze(unittest.TestCase):
    def test_haze(self):
        for test in range(50):
            if random.random() < 0.1:
                nd = None
            else:
                nd = random.randint(-4, 4)
            value = random.randint(0, 10000) + random.random()
            with self.subTest(value=value, nd=nd):
                self.assertEqual(ex4.round_(value, nd), builtin_round(value, nd))


if __name__ == '__main__':
    unittest.main()