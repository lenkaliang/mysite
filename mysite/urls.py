"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, my_homepage_view, current_datetime, hours_ahead, ordering_notice

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^$', my_homepage_view),     # ^$ matches empty
    url(r'^time/$', current_datetime),
    #url(r'^time/plus/\d+/$', hours_ahead), d here is used to match any digit, with '+' is to match any number of digit
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),  # d{1,2} means the digit you pass in the url can be either one digit or two digits
    url(r'^ordering_notice/$', ordering_notice),

]
