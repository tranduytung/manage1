import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import manage1.model as model
from manage1.lib.base import BaseController, render
from manage1.model.meta import Session as Session

log = logging.getLogger(__name__)

class FullcalendarController(BaseController):


    def update_event(self):
        event_id = request.params['event_id']
        start_time = request.params['start_time']
        end_time = request.params['end_time']
        course = model.Session.query(model.Course).filter_by(id = event_id).first()
        from datetime import datetime
        print '---------------'
        print end_time
        course.schedule.end = datetime.strptime(end_time,'%Y-%m-%d-%H:%M:%S')
        print course.schedule.end
        course.schedule.start = datetime.strptime(start_time,'%Y-%m-%d-%H:%M:%S')
        Session.commit()
        return event_id
