# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500365816.28202
_enable_loop = True
_template_filename = '/home/duytung/PycharmProjects/manage1/manage1/templates/student/upload.html'
_template_uri = '/student/upload.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'{% extends "/layout/base.html" %}\n{% block title %}Student - Upload {% endblock %}\n\n{% block content %}\n\n<form method=\'post\' id =\'upload-file\' enctype="multipart/form-data">\n    <input type="hidden" name = \'student_id\' id = \'student_id\' value="{{request.urlvars[\'id\']}}" />\n    <input type="file" name="avatar" id="my_file" />\n    <input type=\'submit\' id=\'upload-file-btn\' value=\'Test button\'/>\n\n    <div id = \'message\'>Initial text</div>\n\n</form>\n{% endblock %}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/student/upload.html", "filename": "/home/duytung/PycharmProjects/manage1/manage1/templates/student/upload.html"}
__M_END_METADATA
"""
