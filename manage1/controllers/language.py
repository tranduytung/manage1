import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from manage1.lib.base import BaseController, render
import manage1.lib.helpers as h

log = logging.getLogger(__name__)

class LanguageController(BaseController):

    def choose(self):
        language = request.params['language']
        print request.language
        session['language'] = language
        session.save()
        redirect(h.url('/'))
