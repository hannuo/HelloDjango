from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view,testdb,search,search2
from django.conf.urls import *
from django.contrib import admin
urlpatterns = [
    #url(r'^$', view.hello),
    #path('hello/',view.hello),
    url(r'^hello$',view.hello),
    url(r'^testdb$',testdb.testdb),
    url(r'^btestdb$',testdb.btestdb),
    url(r'^ctestdb$',testdb.ctestdb),
    url(r'^dtestdb$',testdb.dtestdb),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
    url(r'^search-post$',search2.search_post),
    url(r'^admin/',admin.site.urls),
]
