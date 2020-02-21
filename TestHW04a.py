"""
Test HW04a
"""
import unittest
import requests
from unittest import mock
import HW04a


class TestResult(unittest.TestCase):
    """ test result() """
    @mock.patch('HW04a.result')
    def test_result(self, mockedReq):
        list1 = ['Repo: MLN Number of commits: 30',
                 'Repo: MLNKV Number of commits: 14',
                 'Repo: MLN_Toolkit Number of commits: 10']
        mockedReq.return_value = list1
        self.assertEqual(HW04a.result("momotech"), list2)
        # self.assertEqual(result("John567"), [])

if __name__ == '__main__':
    # test_result("momotech")
    unittest.main(exit=False, verbosity=2)