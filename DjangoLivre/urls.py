"""DjangoLivre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from BancoDjangoLivre.views import CreateUser, UserViewSet, CreateTransfer, TransferViewSet, UserSearch, TransferSearch, AccountViewSet, MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('user/<str:pk>/', UserSearch.as_view()),
    path('create-user/', CreateUser.as_view()),
    path('all-users/', UserViewSet.as_view()),
    path('transfer/', CreateTransfer.as_view()),
    path('all-transfers/', TransferViewSet.as_view()),
    path('transfer/<str:id>/', TransferSearch.as_view()),
    path('account/<str:id>/', AccountViewSet.as_view()),
]
