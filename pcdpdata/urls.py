from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^projects/$',views.inde, name='list-projects'),
    # url(r'^projects/(?P<project_id>\d)/$', views.index, name='get-project'),
    url(r'^assessment/$', views.AssessmentList.as_view(), name='list-assessment'),
    url(r'^assessment/(?P<assessment_id>\d+)/$', views.AssessmentDetail.as_view(), name='get-assessment'),
    # url(r'^results/(?P<assessment_id>)\d+)/$', views.ResultList.as_view(), name='list-results'),
    # url(r'^results/(?P<assessment_id>)\d+)/(?P<user_id>\d+)$', views.ResultDetail.as_view(), name='get-results'),
]
