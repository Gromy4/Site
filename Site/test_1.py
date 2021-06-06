import unittest
import re   
import app

class Test_test1(unittest.TestCase):
        def test_mail_False(self):
            mail = ["","F" "da@","@mail", "@mail.r", "asdf@_ru", "@mail.r", "gmail.com", "as@hgd@ru.mail", "привет@mail.ru", ".@lootfar.ru", "hello@gmail..com"]
            for i in range (len(mail)):
                regex=re.search(r'[a-zA-Z0-9_+-]+[@][a-zA-Z0-9-.]+[^.]\.[a-zA-Z0-9-.]{2,3}$',mail[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertFalse(a)

if __name__ == '__main__':
    unittest.main()