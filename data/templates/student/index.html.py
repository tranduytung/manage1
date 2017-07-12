# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499748002.594134
_enable_loop = True
_template_filename = '/home/duytung/PycharmProjects/manage1/manage1/templates/student/index.html'
_template_uri = '/student/index.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n    <meta charset="utf-8"/>\n    <title>Proba</title>\n</head>\n<body>\n{% for n in range(1,5) %}\n{{n}}\n{% endfor %}\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/student/index.html", "filename": "/home/duytung/PycharmProjects/manage1/manage1/templates/student/index.html"}
__M_END_METADATA
"""
