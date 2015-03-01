from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import books.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books$', books.views.ListBookView.as_view(),
        name = 'list-book'),

    url(r'^books/new$', books.views.NewBookView.as_view(),
        name = 'new-book'),

    url(r'^books/edit/(?P<pk>\d+)/$', books.views.EditBookView.as_view(),
        name = 'edit-book'),
)
