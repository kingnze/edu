from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('tuition_and_payment',views.tuition_and_payment,name='tuition_and_payment'),
    path('tuition_and_payment/<slug:slug_id>/',views.tuition_and_payment,name='tuition_and_payment'),
    path('contact',views.contact,name='contact'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('discipline',views.discipline,name='discipline'),
    path('discipline/<slug:slug_id>/',views.discipline,name='discipline'),
    path('time_table',views.time_table,name='time_table'),
    path('time_table/<slug:slug_id>/',views.time_table,name='time_table'),
    path('staff_members',views.staff_members,name='staff_members'),
    path('management',views.management,name='management'),
    path('dressing/<slug:slug_id>/',views.dressing,name='dressing'),
    path('dressing',views.dressing,name='dressing'),
    path('facilities',views.facilities,name='facilities'),
    path('stats',views.stats,name='stats'),
    path('blogs',views.blogs,name='blogs'),
    path('ourservices',views.ourservice,name='ourservices'),
    path('stats',views.stats,name='stats'),
    path('history/<slug:slug_id>/',views.history,name='history'),
    path('blog/<slug:slug_id>/',views.blog,name='blog'),
    path('ourservices/<slug:slug_id>/',views.ourservices,name='ourservices')
   
]