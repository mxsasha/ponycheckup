from django.conf.urls import *

from views import EnterUrlView, ResultView, ResultAjaxView

urlpatterns = patterns('',
    url(r'^$', EnterUrlView.as_view(), name="enterurl"),
    url(r'^result/$', ResultView.as_view(), name="result"),
    url(r'^result_ajax/$', ResultAjaxView.as_view(), name="result_ajax"),
)
