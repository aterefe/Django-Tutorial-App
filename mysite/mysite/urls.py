"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    3. The include function allows referencing other Urlconf 
"""
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # url for user to interact with the poll or view it
    url(r'^polls/', include('polls.urls')),
    # url for admin to create delete ad update poll
    url(r'^admin/', admin.site.urls),
]

"""
[] - means optional arguments
The url(regex || view,[kwargs, name]) 

url()argument: regex
Regex is regular expression, which is a syntax for matching patterns in url patterns
Starts at the first regular experssion and makes its way down the list, comparing the requested url against each regex until it finds the match
These regular expressions are compiled the first time the URLconf module is loaded(super fast)
!regular expressions do not search GET and POST parameters, or the domain name

url()argument: views
TODO: Will be explained better later on the tutorial

url()argument: kwargs
?Arbitrary keyword arguments can be passed in a dictionary to the target view. 

url()argument: name
Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates.
!make global changes to the URL patterns of your project while only touching a single file
"""
