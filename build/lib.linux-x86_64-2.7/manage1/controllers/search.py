import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import manage1.model as model
from manage1.model.meta import Session
from pylons.decorators.rest import restrict

from manage1.lib.base import BaseController, render_jinja

log = logging.getLogger(__name__)


class SearchController(BaseController):
    @restrict('GET')
    def student(self):
        if request.params:
            email = request.params['email']
            name = request.params['name']
            if not email and not name:
                c.students = []
            else:
                c.students = Session.query(model.Student)
                if email:
                    c.students = c.students.filter(model.Student.email.like('%'+email+'%'))
                if name:
                    c.courses = c.students.filter(model.Student.name.like('%'+name+'%'))
                c.students = c.students.all()
            c.form_result = request.params
        return render_jinja('/search/student.html')

    @restrict('GET')
    def course(self):
        if request.params:
            code = request.params['code']
            name = request.params['name']
            if not code and not name:
                c.courses = []
            else:
                c.courses = Session.query(model.Course)
                if code:
                    c.courses = c.courses.filter(model.Course.code.like('%'+code+'%'))
                if name:
                    c.courses = c.courses.filter(model.Course.name.like('%'+name+'%'))
                c.courses = c.courses.all()
            c.form_result = request.params
        return render_jinja('/search/course.html')
