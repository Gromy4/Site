import unittest
import re
import app

class Test_test4(unittest.TestCase):
        def test_phone_True(self):
            phone = ["8-931-233-49-72"]
            for i in range (len(phone)):
                regex=re.search(r'^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$',phone[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()