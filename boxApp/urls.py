from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.box_list),
    path('type/list/', views.producttype_list),
    path('type/<str:pk>', views.producttype_detail),
    path('task/<int:task>', views.test_tasks),
]