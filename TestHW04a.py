"""
Test HW04a
"""
import unittest
from HW04a import result

class TestResult(unittest.TestCase):
    """ test result() """
    def testResult(self):
        list1 = ['Repo: cs61b Number of commits: 2', 'Repo: HW09 Number of commits: 2',
                 'Repo: SSW567 Number of commits: 2', 'Repo: SSW810 Number of commits: 2',
                 'Repo: Triangle567 Number of commits: 2']
        self.assertEqual(result("deng125125"), list1)
        self.assertEqual(result("John567"), [])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)