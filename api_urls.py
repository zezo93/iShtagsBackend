"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from users.views import UserRetrieveAPIView, LoginView

# here we will add our api urls for ishtags apis
urlpatterns = [
    url(r'^users/(?P<user_id>[0-9]+)/$',
        UserRetrieveAPIView.as_view()),
    url(r'^login/local/$',
        LoginView.as_view()),

]
