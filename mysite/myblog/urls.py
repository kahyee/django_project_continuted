from django.conf.urls import url
from myblog.views import stub_view
from myblog.views import detail_view, BlogIndex, add_model

urlpatterns = [
    url(r'^$',
        BlogIndex.as_view(),
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),
    url(r'^add',
        add_model,
        name="add_post")
]