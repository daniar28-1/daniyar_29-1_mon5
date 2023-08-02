"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views
from users.views import register, confirm_user, authenticate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors', views.list_director_api_view),
    path('api/v1/directors/<int:id>/', views.director_detail_api_view),
    path('api/v1/movies', views.list_Movie_api_view),
    path('api/v1/movies/<int:id>/', views.moive_detail_api_view),
    path('api/v1/reviews', views.List_Review_api_view),
    path('api/v1/directors/<int:id>/', views.review_detail_api_view),
    path('api/v1/movies/reviews/', views.movies_reviews_api_view),
    path('api/v1/users/register/', register),
    path('api/v1/users/authenticate', authenticate),
    path('api/v1/users/confirm', confirm_user),

]
