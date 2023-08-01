# Name: Aaron Anderson
# Class: CS362 Software Engineering II
# Assignment: A2 TDD Hands ON
# Date: 08/01/2023 (Received an Extension from Professor Ianni)


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test_1(self):
        pwd = ""
        self.assertFalse(check_pwd(pwd))
        check_pwd(pwd)


if __name__ == '__main__':
    unittest.main()
