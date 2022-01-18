from django.urls import path
from . import views
from .views import (
    LogListView,
    LogCreateView,
    LogDetailView
)

urlpatterns = [
    path('', views.home, name='weightloss-home'),
    path('log/', LogListView.as_view(), name='weightloss-log'),
    path('log/<int:pk>', LogDetailView.as_view(), name='weightloss-log-detail'),
    path('post/', LogCreateView.as_view(), name='weightloss-post'),
    path('guide/', views.guide, name='weightloss-guide'),

]