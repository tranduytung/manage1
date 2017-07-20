import logging
import os
import random

from formencode import htmlfill
from pylons import config
import shutil
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate

import manage1.lib.helpers as h
from manage1.lib.base import BaseController, render, render_jinja
from manage1.model.meta import Session as Session
import manage1.model as model
from manage1.form.new_student_form import NewStudentForm
import formencode

log = logging.getLogger(__name__)


class StudentController(BaseController):
    def index(self):
        c.students = Session.query(model.Student).all()
        if request.params:
            page = request.params['page']
        else:
            page = 1
        c.students = paginate.Page(c.students, page=page, items_per_page=10)
        return render_jinja('/student/index.html')

    def show(self, id):
        c.student = Session.query(model.Student).filter_by(id=id).first()
        if not c.student:
            abort(404, '404 Not Found')
        c.courses = Session.query(model.Course).all()
        return render_jinja('/student/show.html')

    def new(self):
        return render_jinja('/student/new.html')

    def create(self):
        schema = NewStudentForm()
        try:
            form_result = schema.to_python(request.params)
        except formencode.validators.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            h.flash('Tao moi that bai', 'error')
            return render_jinja('/student/new.html')
        else:
            email = request.params['email']
            name = request.params['name']
            password = request.params['password']
            Session.add(model.Student(name=name, email=email, password=password))
            Session.commit()
            h.flash('Tao moi thanh cong', 'success')
            return redirect(url(controller='student', action='index'))

    def edit(self, id):
        schema = NewStudentForm()
        student = Session.query(model.Student).filter_by(id=id).first()
        if not student:
            abort(404, '404 Not Found')
        # c.form_result = schema.from_python(student.__dict__)
        c.form_result = student.__dict__
        c.form_errors = {}
        c.id = int(id)
        return render_jinja('/student/edit.html')

    @restrict('POST')
    def update(self, id=None):
        schema = NewStudentForm()
        student = Session.query(model.Student).filter_by(id=id).first()
        c.id = int(id)
        if not student:
            abort(404, '404 Not Found')
        try:
            form_result = schema.to_python(request.params, c)
        except formencode.validators.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            h.flash('Edit that bai', 'error')
            return render_jinja('/student/edit.html')
        else:
            student.email = request.params['email']
            student.name = request.params['name']
            student.password = request.params['password']
            Session.commit()
            h.flash('Edit thanh cong', 'success')
            return redirect(url(controller='student', action='index'))

    def delete(self, id):
        student = Session.query(model.Student).filter_by(id=id).first()
        if not student:
            abort(404, '404 Not Found')
        Session.delete(student)
        Session.commit()
        h.flash('Xoa student thanh cong', 'success')
        return redirect(h.url(controller='student', action='index'))

    #
    def upload(self, id):
        c.student = Session.query(model.Student).filter_by(id=id).first()
        return render_jinja('/student/upload.html')

    def save_avatar(self):
        print('tung')
        id = request.POST['student_id']
        c.student = Session.query(model.Student).filter_by(id=id).first()
        my_file = request.POST['file']
        my_file.filename = str(random.getrandbits(64)) + my_file.filename
        permanent_file = open(
            os.path.join(
                config['app_conf']['temporary_store'],
                my_file.filename.replace(os.sep, '_')
            ),
            'wb'
        )
        shutil.copyfileobj(my_file.file, permanent_file)
        c.student.avatar = my_file.filename
        Session.commit()
        my_file.file.close()
        permanent_file.close()
        return h.image_name(c.student)
