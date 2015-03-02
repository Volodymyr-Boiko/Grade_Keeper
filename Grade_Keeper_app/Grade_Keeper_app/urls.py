from django.conf.urls import patterns, url
from Grade_Keeper_app import views

urlpatterns = patterns('',
                       url(r'^$', views.main_assignments, name='main_assignments'),
                       url(r'^assignment/(?P<assign_id>\d+)$', views.assignments, name='assignments'),
                       url(r'^assignment/(?P<assign_id>\d+)/add_student$', views.add_student, name='add_student'),
                       url(r'^add_assigment/$', views.add_assigment, name='add_assigment'),
                       url(r'^delete/$', views.delete, name='delete'),
                       url(r'^assignment/(?P<assign_id>\d+)/edit_student/(?P<st_id>\d+)$', views.edit_student, name='edit_student'),
                       )
