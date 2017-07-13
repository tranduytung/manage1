import formencode
# from manage1.model.simple_email import SimpleEmail
from manage1.validation.unique_code import UniqueCode
from manage1.validation.format_code import FormatCode

class NewCourseForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    code = formencode.All(formencode.validators.String(not_empty = True), FormatCode, UniqueCode)
    name = formencode.validators.String(not_empty = True)
    number = formencode.validators.Number(not_empty = True, max= 1000, min = 0)
