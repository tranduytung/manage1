"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
import hashlib
import urllib
from manage1.lib import auth
from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *
from pylons import url
from webhelpers.pylonslib.flash import Flash as _Flash
flash = _Flash()


def create_students_options(type_list):
    options = [(ct.id, ct.user_info.name+'--'+ ct.email) for ct in type_list]
    return Options(options)

def create_courses_options(type_list):
    options = [(ct.id, ct.code+'--'+ ct.name) for ct in type_list]
    return Options(options)

def image_name(student):
    gravatar_id = student.email
    if student.user_info and student.user_info.avatar:
        return '/upload/temporary/'+student.user_info.avatar
    else:
        gravatar_url = 'https://www.gravatar.com/avatar/' + hashlib.md5(gravatar_id.lower()).hexdigest() + '?'
        return gravatar_url

def send_mail(SUBJECT, BODY, FROM, TO):
    print 'tung1'
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.text import MIMEText
    # import smtplib
    # gmail_password = 'tranduytung27011994'
    # msg = MIMEMultipart()
    # msg['From'] = FROM
    # msg['To'] = TO
    # msg['Subject'] = SUBJECT
    # HTML_BODY = MIMEText(BODY, 'html')
    # msg.attach(HTML_BODY)
    # print 'tung2'
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.ehlo()
    # server.login(FROM, gmail_password)
    # server.sendmail(FROM, TO, msg.as_string())
    # server.close()
    # return 'tung3'