import unittest
import inclassactivitycalc

class testCaseCalc(unittest.TestCase):
    def test_add(self):
        result = inclassactivitycalc.add(10000000000000000000000000000000000000000,5)
        result1 = inclassactivitycalc.sub(10,5)
        result2 = inclassactivitycalc.mul(10,5)
        result3 = inclassactivitycalc.div(10,5)
        self.assertEqual(result,10000000000000000000000000000000000000005)
        self.assertEqual(result1,5)
        self.assertEqual(result2,50)
        self.assertEqual(result3,2.0)

if __name__ == '__main__':
    unittest.main();