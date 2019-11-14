from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index "),
    # the ^$ mean don't add anything to URL'
    # name means the name of the thing we want to display
    # views.index means we're calling index function from views

    # for details function/view
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
    # initializing a URL
    # creating a string defined by question mark P
    # id should be 0-9
    # 127.0.0.1/polls/1

    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name = "results"),
    # 127.0.0.1/polls/1.results

    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name = "vote")
    # 127.0.0.1/polls/1/votes
]