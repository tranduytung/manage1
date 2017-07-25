import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import manage1.lib.helpers as h
from manage1.model import meta
import manage1.model as model
# from authkit.users import Users
from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import ValidAuthKitUser

from manage1.lib.base import BaseController, render_jinja

log = logging.getLogger(__name__)

class AccountController(BaseController):
    def __before__(self, action, **params):
        user = session.get('user')
        if user:
            request.environ['REMOTE_USER'] = user.email
        c.users = request.environ['authkit.users']

    def signin(self):
        print (request.params)
        if request.params:
            print (request.params['username'])
            print c.users
            if c.users:
                session['user'] = meta.Session.query(model.Users).filter_by(email = 'admin').first()
                session.save()
                return redirect(h.url(controller='account', action="signedin"))
            else:
                return render_jinja('/derived/account/signin.html')
        else:
            return render_jinja('/derived/account/signin.html')

    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        request.environ['authkit.users'] = ''
        del session['user']
        return render_jinja('/derived/account/signedout.html')

    @authorize(ValidAuthKitUser())
    def signedin(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        # request.environ['REMOTE_USER'] = request.environ['authkit.users']
        print(request.environ['authkit.users'].role_exists('admin'))
        # print(1)
        # print(authorize(h.auth.has_auth_kit_role('admin')))
        return render_jinja('/derived/account/signedin.html')