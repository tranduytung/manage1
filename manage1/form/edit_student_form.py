import formencode
# from manage1.model.simple_email import SimpleEmail
from manage1.validation.unique_email import UniqueEmail
from manage1.validation.secure_password import SecurePassword

class EditStudentForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.All(formencode.validators.Email(not_empty = True), UniqueEmail)
    name = formencode.validators.PlainText(not_empty = True)
    password = SecurePassword()
    password_confirm = formencode.validators.ByteString(not_empty = True)
    chained_validators = [formencode.validators.FieldsMatch('password', 'password_confirm')]
