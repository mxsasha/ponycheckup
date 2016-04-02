# Create your views here.
import datetime
import time
from django.views.generic.base import TemplateView
import re
from .models import Check
from .checker import SecurityChecker

MINIMAL_CHECK_TIME = 2.5


class EnterUrlView(TemplateView):
    template_name = 'check/enter_url.html'


class ResultView(TemplateView):
    template_name = 'check/result.html'


class ResultAjaxView(TemplateView):
    template_name = 'check/result_ajax.html'

    def dispatch(self, request, *args, **kwargs):
        start_time = time.time()
        response = super(ResultAjaxView, self).dispatch(request, *args, **kwargs)
        wait_time = start_time + MINIMAL_CHECK_TIME - time.time()
        if wait_time > 0:
            time.sleep(wait_time)
        return response

    def get_context_data(self, **kwargs):
        context = super(ResultAjaxView, self).get_context_data(**kwargs)

        try:
            url = self.request.GET['url']
        except KeyError:
            context['could_not_load'] = True
            return context

        url = self.sanitize_url(url)
        if not url:
            context['could_not_load'] = True
            return context

        checker = SecurityChecker()
        force_refresh = self.request.GET.get('force_refresh', None)

        existing_objects = Check.objects.filter(url=url)
        if not force_refresh and len(existing_objects) and datetime.datetime.now()-existing_objects[0].created < datetime.timedelta(minutes=5):
            check_result = existing_objects[0]
            context['reused_existing_object'] = True
        else:
            check_result = checker.run_check(url)

        if check_result and isinstance(check_result, Check):
            context['check_record'] = check_result
            percentage = check_result.secure_percentage

            if percentage >= 85:
                context['score_good'] = True
            elif percentage >= 50:
                context['score_warning'] = True
            else:
                context['score_bad'] = True

        else:
            context['could_not_load'] = True
            context['error'] = check_result
        return context

    def sanitize_url(self, url):
        url = re.sub("http.?://", '', url)
        url = url.split("/")[0]
        if not re.match("^[A-z0-9\.-]+$", url):
            return False

        return "http://"+url
