# coding=utf-8;

__author__ = 'skhaylov'


from django.views.generic import View

from .mixins import JSONMixin, JSONUpdateMixin, CSRFExemptMixin


class JSONView(JSONMixin, View):
    def dispatch(self, request, *args, **kwargs):
        from django.conf import settings

        try:
            return super(JSONView, self).dispatch(request, *args, **kwargs)
        except Exception as exc:
            if settings.DEBUG:
                import traceback

                var = traceback.format_exc()
                # TODO: Use logging
                print str(exc)
                print var
            return self.render_to_response(None)

    def get(self, request, *args, **kwargs):
        context = self.get_json_context()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_json_context()
        return self.render_to_response(context)


class JSONUpdateView(JSONUpdateMixin, JSONView):
    def post(self, request, *args, **kwargs):
        self.process()
        return super(JSONUpdateView, self).post(request, * args, **kwargs)


class CSRFExemptJSONView(CSRFExemptMixin, JSONView):
    pass


class CSRFExemptJSONSaveView(CSRFExemptMixin, JSONUpdateView):
    pass
