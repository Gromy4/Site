import unittest
import re
import app

class Test_test2(unittest.TestCase):
        def test_mail_True(self):
            mail = ["Petya.Petrov@mail.ru","Gromy4@mail.ru","adf.d.d.fgs.a@mail.ru","Korolev_Roman.821@gmail.com"]
            for i in range (len(mail)):
                regex=re.search(r'[a-zA-Z0-9_+-]+[@][a-zA-Z0-9-.]+[^.]\.[a-zA-Z0-9-.]{2,3}$',mail[i])
                if (regex == None):
                    a=False
                if (regex != None):
                    a=True
                self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()