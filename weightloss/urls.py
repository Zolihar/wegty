from django.urls import path
from . import views
from .views import (
    LogListView,
    LogCreateView,
    LogDetailView,
    LogDeleteView,
    LogUpdateView,
    ChecklistCreateView,
    ChecklistUpdateView,
)

urlpatterns = [
    path('', views.home, name='weightloss-home'),
    path('log/', LogListView.as_view(), name='weightloss-log'),
    path('log/<int:pk>', LogDetailView.as_view(), name='weightloss-log-detail'),
    path('log/<int:pk>/delete', LogDeleteView.as_view(), name='weightloss-log-delete'),
    path('log/<int:pk>/update', LogUpdateView.as_view(), name='weightloss-log-update'),
    path('post/', LogCreateView.as_view(), name='weightloss-post'),
    path('graph/', views.graph, name='weightloss-graph'),
    path('checklist/', views.checklist, name='weightloss-checklist'),
    path('checklist/create', ChecklistCreateView.as_view(), name='weightloss-checklist-create'),
    path('checklist/update/<int:pk>', ChecklistUpdateView.as_view(), name='weightloss-checklist-update'),

]