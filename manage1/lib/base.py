"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons.templating import render_jinja2 as render_jinja
from jinja2 import Environment, PackageLoader, select_autoescape
from manage1.model.meta import Session
from pylons import request, response, session, tmpl_context as c, url
from pylons.i18n.translation import _, set_lang
import manage1.model as model

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        # def __before__(self, action, **params):
        user = session.get('user')
        set_lang('es')
        c.activities = model.Session.query(model.Activity).\
            order_by(model.Activity.created_at.desc()).all()
        c.model = model
        if user:
            request.environ['REMOTE_USER'] = user.email
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()
