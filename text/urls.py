from importlib.resources import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'text'
urlpatterns = [
    path('', views.index, name="index"),
    path('ret', views.index, name="ret"),
    path('s1', views.s1, name='s1'),
    path('s2', views.s2, name='s2'),
    path('s3', views.s3, name='s3'),
    path('s5', views.s5, name='s5'),
    path('s6', views.s6, name='s6'),
    path('s7', views.s7, name='s7'),

    path('textcollect',
         views.textcollect, name='textcollect'),
    path('<int:question_id>/text', views.text, name='text'),

    path('<int:question_id>/textva', views.textva, name='textva'),
    path('<int:question_id>/textvb', views.textvb, name='textvb'),
    path('<int:question_id>/ans', views.ans, name='ans'),

    path('textcollect2',
         views.textcollect2, name='textcollect2'),
    path('<int:question_id>/text2', views.text2, name='text2'),

    path('<int:question_id>/textva2', views.textva2, name='textva2'),
    path('<int:question_id>/textvb2', views.textvb2, name='textvb2'),
    path('<int:question_id>/ans2', views.ans2, name='ans2'),
    path('tenki', views.tenki_show, name="tenki_show"),
    path('move_to_gamepage', views.move_to_gamepage, name="move_to_gamepage"),



    path('test', views.HomeView.as_view(), name='test')



]
