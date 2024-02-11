from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddCourseView.as_view(), name='add_course'),
    path('course/<int:pk>', views.DetailCourseView.as_view(), name='course_detail')
]
