# coding=utf-8;

__author__ = 'skhaylov'

import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from json_response import JSONResponse


class JSONMixin(object):
    response_class = JSONResponse

    def get_json_context(self):
        context = super(JSONMixin, self).get_json_context()

        return context

    def get_json_request(self, request_key):
        data = getattr(self.request, self.request.method)
        return json.loads(data[request_key])

    def render_to_response(self, context, **kwargs):
        return self.response_class(context, **kwargs)


class JSONUpdateMixin(object):
    def process(self):
        super(JSONUpdateMixin, self).process()


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(request, *args, **kwargs)
