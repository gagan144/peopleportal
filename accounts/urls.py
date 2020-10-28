from django.urls import path

from accounts import views


urlpatterns = [
    path('login/', views.login, name="accounts__login"),
    path('logout/', views.logout, name="accounts__logout"),
]