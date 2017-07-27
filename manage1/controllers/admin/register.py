import logging

from authkit.authorize.pylons_adaptors import authorize
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from manage1.model.meta import Session
import manage1.model as model
import manage1.lib.helpers as h

from manage1.lib.base import BaseController, render_jinja

log = logging.getLogger(__name__)

class RegisterController(BaseController):

    @authorize(h.auth.has_admin_role)
    def new(self):
        student_group_id = Session.query(model.Group).filter_by(name='student').first().uid
        c.students = Session.query(model.Users).filter_by(group_id=student_group_id).all()
        c.courses = Session.query(model.Course).all()
        c.registers = Session.query(model.association_table).all()
        c.model = model
        return render_jinja('/admin/register/new.html')

    @authorize(h.auth.has_admin_role)
    def create(self):
        student = Session.query(model.Users).filter_by(id=request.params['student_id']).first()
        if not student:
            abort(404, '404 Student Not Found')
            return redirect(h.url(controller='student', action='index'))
        course_id = request.params['course_id']
        course = Session.query(model.Course).filter_by(id=course_id).first()
        if not course:
            abort(404, '404 Course Not Found')
            return redirect(h.url(controller='course', action='index'))
        register = Session.query(model.association_table).filter_by(user_id=student.id,
                                                                    course_id=course_id).first()
        if register:
            h.flash('Da dang ki tu truoc', 'error')
        else:
            student.courses.append(course)
            Session.commit()
            h.flash('Dang ki thanh cong', 'success')
        return redirect(url(controller='admin/register', action='new', id=student.id))

    @authorize(h.auth.has_admin_role)
    def delete(self):
        student = Session.query(model.Users).filter_by(id=request.params['student_id']).first()
        if not student:
            abort(404, '404 Student Not Found')
        course = Session.query(model.Course).filter_by(id=request.params['course_id']).first()
        if not course:
            abort(404, '404 Course Not Found')
        register = Session.query(model.association_table).filter_by(user_id=student.id,
                                                                    course_id=course.id).first()
        if not register:
            abort(404, '404 Register Not Found')
        student.courses.remove(course)
        Session.commit()
        h.flash('Xoa dang ki thanh cong', 'success')
        return redirect(h.url(controller='admin/register', action='new'))


