import unittest
import re
import app

class Test_test3(unittest.TestCase):
        def test_phone_False(self):
            phone = ["+7 921 344 56 43","8 931 233 497", "8931 2334972", "+7-9312-233-49-72"]
            for i in range (len(phone)):
                regex=re.search(r'^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$',phone[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertFalse(a)

if __name__ == '__main__':
    unittest.main()