from django.urls import path
from . import views


#survey/5/
#survey/5/result
#survey/5/vote
app_name = "survey"
urlpatterns = [
                path('',views.index, name='index'),
                path('<int:question_id>/',views.detail,name = 'detail'),
                path('<int:question_id>/result/',views.result,name='result'),
                path('<int:question_id>/vote/',views.vote,name='vote'),
]