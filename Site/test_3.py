import unittest
import re
import app

class Test_test3(unittest.TestCase):
        def test_phone_False(self):
            phone = ["+32 323 32 32", "8 9222 23 23 45"]
            for i in range (len(phone)):
                regex=re.search(r'^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$',phone[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertFalse(a)

if __name__ == '__main__':
    unittest.main()