from bottle import post, request, route, run, redirect,put

import re

import pdb

import json

@post('/companies', method="post")

def Entry_form():

    partner = request.forms.get('Partners') 

    partnersAbout = request.forms.get('PartnersAbout')

    mail = request.forms.get('Mail') 

    phonenumber = request.forms.get('Phonenumber') 


    regexMail = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+[^.]\.[a-zA-Z0-9]{2,3}$'

    regexPhone = '^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$'

    if len(partner) == 0 or len(partnersAbout) == 0 or len(mail) == 0 or len(phonenumber) == 0:

        return "Empty form!"

    else:

        if (re.search(regexMail, mail) and re.search(regexPhone, phonenumber)):

            with open ('static/content/test.txt', 'a') as outfile:

                open('static/content/test.txt', 'a').write(partner + '\n' + partnersAbout + '\n' + mail + '\n' + phonenumber + '\n' + "*****" + '\n')

            return "New parthner added"

        else:

            return "Data doesn`t match"