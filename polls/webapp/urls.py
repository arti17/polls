from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollView.as_view(), name='index'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='poll_detail'),
    path('poll/create/', views.PollCreateView.as_view(), name='create_poll'),
    path('poll/update/<int:pk>', views.PollUpdateView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>', views.PollDeleteView.as_view(), name='delete_poll'),
    path('choice/create/<int:pk>', views.ChoiceCreateView.as_view(), name='create_choice'),
    path('choice/update/<int:pk>', views.ChoiceUpdateView.as_view(), name='update_choice'),
    path('choice/delete/<int:pk>', views.ChoiceDeleteView.as_view(), name='delete_choice'),
    path('pass_the_poll/<int:pk>', views.AnswerView.as_view(), name='pass_the_poll'),
    path('statistics/<int:pk>', views.StatisticsView.as_view(), name='statistics'),
]
