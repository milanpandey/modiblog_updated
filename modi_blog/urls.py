from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_entry.views.index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/$', 'blog_entry.views.posts_list'),
    url(r'^posts/(?P<pk>.+)/$', 'blog_entry.views.post_detail')
)
