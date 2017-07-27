import logging

from authkit.authorize.pylons_adaptors import authorize
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict

from manage1.model.meta import Session
import manage1.model as model
import manage1.lib.helpers as h
import formencode

from manage1.lib.base import BaseController, render_jinja

log = logging.getLogger(__name__)


class RegisterController(BaseController):

    @authorize(h.auth.is_valid_user)
    @restrict('POST')
    def create(self):
        student = Session.query(model.Users).filter_by(email=request.environ['REMOTE_USER']).first()
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
        return redirect(url(controller='student', action='show', id=student.id))

    def delete(self):
        student = Session.query(model.Users).filter_by(email = request.environ['REMOTE_USER']).first()
        if not student:
            abort(404, '404 Student Not Found')
        course_id = request.params['course_id']
        course = Session.query(model.Course).filter_by(id=course_id).first()
        if not course:
            abort(404, '404 Course Not Found')
        register = Session.query(model.association_table).filter_by(user_id=student.id,
                                                                    course_id=course_id).first()
        if not register:
            abort(404, '404 Register Not Found')
        student.courses.remove(course)
        Session.commit()
        h.flash('Xoa dang ki thanh cong', 'success')
        return redirect(h.url(controller='student', action='show', id=student.id))
