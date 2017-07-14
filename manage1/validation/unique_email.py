import manage1.model as model
from manage1.model.meta import Session as Session
import formencode


class UniqueEmail(formencode.validators.Email):

    def _to_python(self, value, c):
        users_email = Session.query(model.Student).filter_by(email = value).first()
        if users_email > 0 and hasattr(c, 'id') and c.id != users_email.id:
            raise formencode.Invalid('That username already exists', value, c)
        if users_email > 0 and not hasattr(c, 'id'):
            raise formencode.Invalid('That username already exists', value, c)
        return formencode.validators.Email._to_python(self, value, c)
