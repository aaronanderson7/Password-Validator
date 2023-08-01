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

    def test_2(self):
        pwd = ""
        self.assertEqual(check_pwd(pwd), False)

    def test_3(self):
        pwd = "Anderson7!"
        self.assertTrue(check_pwd(pwd))

    def test_4(self):
        pwd = "OregonStateUniversityAaronAnderson7!"
        self.assertFalse(check_pwd(pwd))

    def test_5(self):
        pwd = "ANDERSON7!"
        self.assertFalse(check_pwd(pwd))

    def test_6(self):
        pwd = "anderson7!"
        self.assertFalse(check_pwd(pwd))

    def test_7(self):
        pwd = "Anderson!"
        self.assertFalse(check_pwd(pwd))

    def test_8(self):
        pwd = "Anderson7"
        self.assertFalse(check_pwd(pwd))

    def test_9(self):
        pwd = "TestPassword5@"
        self.assertTrue(check_pwd(pwd))

    def test_10(self):
        pwd = "TestPassword5?"
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()
