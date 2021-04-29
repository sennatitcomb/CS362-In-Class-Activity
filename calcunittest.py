import unittest
import inclassactivitycalc

class testCaseCalc(unittest.TestCase):
    def test_1(self):
        result = inclassactivitycalc.add(5,5)
        self.assertEqual(result,10)
    def test_2(self):
       result = inclassactivitycalc.sub(10,5)
       self.assertEqual(result,5)
    def test_3(self):
        result = inclassactivitycalc.mul(12,5)
        self.assertEqual(result,60)
    def test_4(self):
        result = inclassactivitycalc.div(10,5)
        self.assertEqual(result,2.0)
    def test_5(self):
        result = inclassactivitycalc.add(9,5)
        self.assertEqual(result,3) #fail
    def test_6(self):
       result = inclassactivitycalc.sub(8,5)
       self.assertEqual(result,13) #fail
    def test_7(self):
        result = inclassactivitycalc.mul(12,5)
        self.assertEqual(result,0) #fail
    def test_8(self):
        result = inclassactivitycalc.div(10,5)
        self.assertEqual(result,20) #fail

if __name__ == '__main__':
    unittest.main();