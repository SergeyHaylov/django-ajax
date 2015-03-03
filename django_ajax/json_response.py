# coding=utf-8;

__author__ = 'skhaylov'

import json

from django.http import HttpResponse


class JSONResponse(HttpResponse):
    response_data_key = 'data'

    def __init__(self, content, **kwargs):
        """
        :type content: dict
        """
        data = self.get_json_content(content, **kwargs)

        super(JSONResponse, self).__init__(
            content=data,
            status=None,
            content_type='application/json; encoding=utf-8'
        )

    def get_json_content(self, content, **kwargs):
        return json.dumps({self.response_data_key: content}, ensure_ascii=False)