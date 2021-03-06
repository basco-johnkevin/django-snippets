from django.conf.urls import patterns, include, url
from django.conf import settings

from accounts.views import ( 
    LoginView
)
from snippets.views import (
    SnippetsView,
    SnippetDetailsView,
    CreateSnippetView,
    SnippetDeleteView,
    SnippetUpdateView,
    MySnippetsView
)
from app.views import (
    HomeView
)
from tags.views import (
    TagsView, 
    CreateTagView,
    TagSnippetsView
)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^$', 
        HomeView.as_view(),
        name='home'
    ),
    url(
        r'^login/$', 
        LoginView.as_view(),
        name='login'
    ),
    url(
        r'^logout/$', 
        'django.contrib.auth.views.logout',
        {'next_page': settings.LOGIN_URL},
        name='logout'
    ),

    ################################
    # snippets
    ################################
    url(
        r'^snippets/$', 
        SnippetsView.as_view(),
        name='snippets'
    ),
    url(
        r'^snippets/(?P<slug>[-\w]+)/create/$', 
        CreateSnippetView.as_view(),
        name='snippet_create'
    ),  
    url(
        r'^snippets/(?P<slug>[-\w]+)/$', 
        SnippetDetailsView.as_view(),
        name='snippet_details'
    ), 
    url(
        r'^snippets/(?P<slug>[-\w]+)/delete/$', 
        SnippetDeleteView.as_view(),
        name='snippet_delete'
    ),
    url(
        r'^snippets/(?P<slug>[-\w]+)/update/$', 
        SnippetUpdateView.as_view(),
        name='snippet_update'
    ),           
    url(
        r'^(?P<slug>[-\w]+)/snippets/$', 
        MySnippetsView.as_view(),
        name='user_snippets'
    ), 

    ################################
    # tags
    ################################
    url(
        r'^tags/$', 
        TagsView.as_view(),
        name='tags'
    ),
    url(
        r'^tags/(?P<slug>[-\w]+)/create/$', 
        CreateTagView.as_view(),
        name='tag_create'
    ), 
    url(
        r'^tags/(?P<slug>[-\w]+)/snippets/$', 
        TagSnippetsView.as_view(),
        name='tag_snippets'
    ), 
    # url(r'^django_snippets/', include('django_snippets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
