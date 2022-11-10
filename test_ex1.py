import unittest
import ex1
import sys

class TestEx1(unittest.TestCase):
    def test_fib_result_0(self):
        self.assertEqual(ex1.fib(0), 0)

    def test_fib_result_1(self):
        self.assertEqual(ex1.fib(1), 1)

    def test_fib_result_2(self):
        self.assertEqual(ex1.fib(2), 1)

    def test_fib_result_3(self):
        self.assertEqual(ex1.fib(3), 2)

    def test_fib_result_7(self):
        self.assertEqual(ex1.fib(7), 13)

    def test_fib_result_minus_2(self):
        self.assertEqual(ex1.fib(-2), -1)

class TestEx1_Recursion(unittest.TestCase):
    def setUp(self):
        self.safe = sys.getrecursionlimit()
        sys.setrecursionlimit(40) # this is a hackish value guesstimated.
    
    def tearDown(self) -> None:
        sys.setrecursionlimit(self.safe)

    def test_loop_implementation(self):
        """the exercise requires a loop implementation, 
        so set the recursion limit to something artificial low
        and see if the function still works."""
        
        try:
            ex1.fib(50)
        except RecursionError:
            raise AssertionError("ex1.fib() used a suspicious amount of stack. Recursive implementation?")
        
if __name__ == '__main__':
    unittest.main()