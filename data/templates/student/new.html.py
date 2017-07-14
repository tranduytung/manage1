# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1499768958.214372
_enable_loop = True
_template_filename = '/home/duytung/PycharmProjects/manage1/manage1/templates/student/new.html'
_template_uri = '/student/new.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'{% extends "/layout/base.html" %}\n{% block title %}Student - New {% endblock %}\n\n{% block content %}\n    <div class="row">\n        {{ h.form(h.url(controller=\'student\', action=\'create\')) }}\n            {% if c.form_errors %}\n                {% if c.form_errors.has_key(\'email\') %}\n                    <p>{{ c.form_errors[\'email\'] }}</p>\n                {% endif %}\n                {%if c.form_errors.has_key(\'name\') %}\n                    <p>{{ c.form_errors[\'name\'] }}</p>\n                {% endif %}\n                Email Address: {{ h.text(\'email\', value=c.form_result[\'email\'] or \'\') }}\n                Name: {{h.text(\'name\', value=c.form_result[\'name\'] or \'\') }}\n            {% else %}\n                Email: {{ h.text(\'email\') }}\n                Name: {{ h.text(\'name\') }}\n            {% endif %}\n            {{ h.submit(\'\', \'Submit\') }}\n        {{ h.end_form() }}\n    </div>\n{% endblock %}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/student/new.html", "filename": "/home/duytung/PycharmProjects/manage1/manage1/templates/student/new.html"}
__M_END_METADATA
"""
