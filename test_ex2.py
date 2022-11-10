import unittest
import ex2


class TestEx2(unittest.TestCase):
    def test_clip_result_empty(self):
        self.assertEqual(ex2.clip(), [])
    def test_clip_result_1_2_01_0(self):
        self.assertEqual(ex2.clip(1, 2, 0.1, 0), [1, 1, 0.1, 0])
    def test_clip_result_m1_05(self):
        self.assertEqual(ex2.clip(-1, 0.5), [0, 0.5])
    def test_clip_result_m1_05_min_m2(self):
        self.assertEqual(ex2.clip(-1, 0.5, min_=-2), [-1, 0.5])
    def test_clip_result_m1_05_max_03(self):
        self.assertEqual(ex2.clip(-1, 0.5, max_=0.3), [0, 0.3])
    def test_clip_result_m1_05_min_2_max_03(self):
        self.assertEqual(ex2.clip(-1, 0.5, min_=2,max_=3), [2, 2])
   
    
        
if __name__ == '__main__':
    unittest.main()