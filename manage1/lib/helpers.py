"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password
import hashlib
import urllib
from manage1.lib import auth
from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *
from pylons import url
from webhelpers.pylonslib.flash import Flash as _Flash

flash = _Flash()
from pylons import config
from pylons.i18n.translation import _
import manage1.model as model

email_from = 'tranduytung1994@gmail.com'
email_password = 'tranduytung27011994'


def create_students_options(type_list):
    options = [(ct.id, ct.user_info.name + '--' + ct.email) for ct in type_list]
    return Options(options)


def create_courses_options(type_list):
    options = [(ct.id, ct.code + '--' + ct.name + '----' + ct.schedule.type.value) for ct in type_list]
    return Options(options)


def image_name(student):
    gravatar_id = student.email
    if student.user_info and student.user_info.avatar:
        return '/upload/temporary/' + student.user_info.avatar
    else:
        gravatar_url = 'https://www.gravatar.com/avatar/' + hashlib.md5(gravatar_id.lower()).hexdigest() + '?'
        return gravatar_url


def send_mail(SUBJECT, BODY, TO):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = TO
    msg['Subject'] = SUBJECT
    HTML_BODY = MIMEText(BODY, 'html')
    msg.attach(HTML_BODY)
    print 'Start send'
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email_from, email_password)
    server.sendmail(email_from, TO, msg.as_string())
    server.close()
    print 'Send done'


def new_token():
    import random
    import string
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])


def notification(activity_id):
    activity = model.Session.query(model.Activity).filter_by(id=activity_id).first()
    result = ''
    result = activity.user.user_info.name + ' ' + _(activity.action_type.name.lower()) + ' ' + \
             _(activity.object_type.name.lower())
    if activity.object_type == model.ObjectType.COURSE:
        course = model.Session.query(model.Course).filter_by(id=activity.object_id).first()
        result = result + ' ' + course.code + ' ' + _('at') + ' ' + activity.created_at.strftime('%Y/%m/%d - %H:%M')
    return result


def activity_pusher(user_name, action, object_name, object_type, time, object_id):
    import pusher

    pusher_client = pusher.Pusher(
        app_id='384245',
        key='15e72d442d16f43e033c',
        secret='f09b4384a0341259dbbd',
        cluster='ap1',
        ssl=True
    )
    pusher_client.trigger('my-channel', 'my-event',
                          {'user_name': user_name,
                           'action': _(action.lower()),
                           'object_name': object_name,
                           'object_type': _(object_type.lower()),
                           'time': time,
                           'object_id': object_id
                           })
