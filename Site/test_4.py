import unittest
import re
import app

class Test_test3(unittest.TestCase):
        def test_phone_False(self):
            phone = ["+79213445643","89312334972", "8-931-233-49-72", "+7-931-233-49-72"]
            for i in range (len(phone)):
                regex=re.search(r'^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$',phone[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()