from bottle import post, request
import re
import pdb

@post('/home', method='post')
def my_form():

    questions = {}

    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    reg = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+[^.]\.[a-zA-Z0-9]{2,3}$"
   
   
    if (len(mail) == 0) or (len(question) == 0):
        return "Form is empty! Fill the form."
    else:
        if (re.search(reg, mail)):
            questions[mail] = question
            pdb.set_trace()
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Mail doesn`t match to form"
        