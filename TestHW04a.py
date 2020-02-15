"""
Test HW04a
"""
import unittest
from HW04a import result

class TestResult(unittest.TestCase):
    """ test result() """
    def testResult(self):
        list1 = ['Repo: MLN Number of commits: 30',
                 'Repo: MLNKV Number of commits: 14',
                 'Repo: MLN_Toolkit Number of commits: 10']
        self.assertEqual(result("momotech"), list1)
        self.assertEqual(result("John567"), [])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)