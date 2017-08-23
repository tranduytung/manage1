import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict
from webhelpers import paginate

import manage1.lib.helpers as h
from manage1.lib.base import BaseController, render, render_jinja
from manage1.model.meta import Session as Session
import manage1.model as model
from manage1.form.new_course_form import NewCourseForm
import formencode
from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize

log = logging.getLogger(__name__)


class CourseController(BaseController):

    def index(self):
        c.courses = Session.query(model.Course).filter_by(delete=False).all()
        if request.params.has_key('page'):
            page = request.params['page']
        else:
            page = 1
        c.courses = paginate.Page(c.courses, page=page, items_per_page=10)
        return render_jinja('/course/index.html')


    def show(self, id):
        c.course = Session.query(model.Course).filter_by(id=id).first()
        c.model = model
        if not c.course:
            abort(404, '404 Not Found')
        return render_jinja('/course/show.html')

    # @authorize(h.auth.authorized(h.auth.is_valid_user))
    def new(self):
        return render_jinja('/course/new.html')

    def create(self):
        schema = NewCourseForm()
        try:
            form_result = schema.to_python(request.params)
        except formencode.validators.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            h.flash('Tao moi that bai', 'error')
            return render_jinja('/course/new.html')
        else:
            code = request.params['code']
            name = request.params['name']
            number = request.params['number']
            Session.add(model.Course(code=code, name=name, number=number))
            Session.commit()
            h.flash('Tao moi thanh cong', 'success')
            return redirect(url(controller='course', action='index'))

    @authorize(h.auth.is_valid_user)
    def edit(self, id):
        schema = NewCourseForm()
        course = Session.query(model.Course).filter_by(id=id).first()
        if not course:
            abort(404, '404 Not Found')
        c.form_result = schema.from_python(course.__dict__)
        c.form_errors = {}
        return render_jinja('/course/edit.html')

    @authorize(h.auth.has_delete_role)
    @restrict('POST')
    def update(self, id=None):
        schema = NewCourseForm()
        course = Session.query(model.Course).filter_by(id=id).first()
        c.id = int(id)
        if not course:
            abort(404, '404 Not Found')
        try:
            print(request.params)
            form_result = schema.to_python(request.params, c)
        except formencode.validators.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            h.flash('Edit that bai', 'error')
            return render_jinja('/course/edit.html')
        else:
            course.code = request.params['code']
            course.name = request.params['name']
            course.number = request.params['number']
            remote_user = model.Session.query(model.Users). \
                filter_by(email=request.environ['REMOTE_USER']).first()
            activity = model.Activity(action_type=model.ActionType.EDIT,
                                      object_id=course.id,
                                      object_type=model.ObjectType.COURSE)
            remote_user.activities.append(activity)
            Session.commit()
            h.flash('Edit thanh cong', 'success')
            return redirect(url(controller='course', action='index'))

    @authorize(h.auth.has_delete_role)
    def delete(self, id):
        course = Session.query(model.Course).filter_by(id=id, delete=False).first()
        if not course:
            abort(404, '404 Not Found')
        remote_user = model.Session.query(model.Users).\
            filter_by(email=request.environ['REMOTE_USER']).first()
        activity = model.Activity(action_type=model.ActionType.DELETE,
                                  object_id=course.id,
                                  object_type=model.ObjectType.COURSE)
        remote_user.activities.append(activity)
        self.__add_pusher(remote_user.user_info.name,
                          action= activity.action_type.name,
                          object_name= course.code,
                          object_type = activity.object_type.name,
                          time= activity.created_at.strftime('%Y/%m/%d - %H:%M'),
                          object_id = course.id)
        course.delete = True
        Session.commit()
        h.flash('Xoa course thanh cong', 'success')
        return redirect(h.url(controller='course', action='index'))

    def __add_pusher(self, user_name, action, object_name, object_type, time, object_id):
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
                               'action': action,
                               'object_name': object_name,
                               'object_type': object_type,
                               'time': time,
                               'object_id': object_id
                               })
