import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from webhelpers import paginate
import manage1.lib.helpers as h
import manage1.model as model
from manage1.lib.base import BaseController, render_jinja
from dateutil.relativedelta import relativedelta

log = logging.getLogger(__name__)

class CourseController(BaseController):

    def index(self):
        c.courses = model.Session.query(model.Course).all()
        if request.params.has_key('page'):
            page = request.params['page']
        else:
            page = 1
        c.courses = paginate.Page(c.courses, page=page, items_per_page=10)
        return render_jinja('/admin/courses/index.html')

    from pylons.decorators import jsonify
    @jsonify
    def eventfeeds(self):
        result = []
        default_date = request.params['default_date']
        from datetime import datetime
        default_date = datetime.strptime(default_date, '%Y-%m-%d')
        courses = model.Session.query(model.Course).all()
        start_month = default_date.replace(day=15, month=default_date.month - 1)
        end_month = default_date.replace(month=default_date.month + 1,
                                         day=15, hour=23, minute=59, second=59)
        for course in courses:
            type = course.schedule.type
            start = course.schedule.start
            end = course.schedule.end
            if type == model.ScheduleType.NO_REPEAT:
                if start <= end_month or end >= start_month:
                    result.append({
                        'id': course.id,
                        'title': course.code,
                        'name': course.name,
                        'start': str(course.schedule.start),
                        'end': str(course.schedule.end),
                        'type': 0,
                        'url': h.url(controller='course', action='show', id=course.id)
                    })
            else:
                end_repeat = course.schedule.end_repeat
                while (start.date() <= end_repeat) and \
                        (start < end_month or (end > start_month and end < end_month)):
                    result.append({
                        'id': course.id,
                        'name': course.name,
                        'title': course.code,
                        'start': str(start),
                        'end': str(end),
                        'type': 1,
                        'url': h.url(controller='course', action='show', id=course.id),
                    })
                    if type == model.ScheduleType.WEEKLY:  # repeat weekly
                        start = start + relativedelta(weeks=1)
                        end = end + relativedelta(weeks=1)
                    elif type == model.ScheduleType.MONTHLY:  # repeat monthly
                        start = start + relativedelta(months=1)
                        end = end + relativedelta(months=1)
        return result

