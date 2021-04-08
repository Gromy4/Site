from bottle import post, request
import re

@post('/home', method='post')
def my_form():

    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')

    reg = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]+\w{2,3}$'
   
    if (len(mail) == 0) or (len(question) == 0):
        return "Form is empty! Fill the form."
    else:
        if (re.search(reg, mail)):
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Mail doesn`t match to form"
        