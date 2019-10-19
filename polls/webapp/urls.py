from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollView.as_view(), name='index'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='poll_detail'),
    path('poll/create/', views.PollCreateView.as_view(), name='create_poll'),
    path('poll/update/<int:pk>', views.PollUpdateView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>', views.PollDeleteView.as_view(), name='delete_poll'),
]
