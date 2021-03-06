 
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /agora/
    url(r'^$', views.index, name='index'),
    # ex: /agora/new_user/
    url(r'^new_user/$', views.new_user, name='new_user'),
    # ex: /agora/login/
    url(r'^login/$', views.login_user, name='login'),
    # ex: /agora/logout/
    url(r'^logout/$', views.logout_user, name='logout'),
    # ex: /agora/all_topics/
    url(r'^all_topics/$', views.all_topics, name='all_topics'),
    # ex: /agora/topics/5/sort/sort-method
    #(?P<page_slug>[\w-]+)
    url(r'^all_topics/sort/(?P<sort_method>[\w-]+)/$', views.all_topics, name='all_topics'),
    # ex: /agora/topics/
    url(r'^topics/$', views.all_topics, name='all_topics'),
    # ex: /agora/topics/5/
    url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topics, name='topics'),
    # ex: /agora/users/
    url(r'^users/$', views.view_users, name='users'),
    # ex: /agora/user/5/
    url(r'^user/(?P<user_id>[0-9]+)/$', views.view_user, name='user'),
    # ex: /agora/topics/5/sort/sort-method
    #(?P<page_slug>[\w-]+)
    url(r'^topics/(?P<topic_id>[0-9]+)/sort/(?P<sort_method>[\w-]+)/$', views.topics, name='topics'),
    # ex: /agora/topics/new/
    url(r'^topics/new/$', views.new_topic, name='newtopic'),
    # ex: /agora/topics/new/
    url(r'^topics/new/(?P<parent_topic_id>[0-9]+)/$', views.new_topic, name='newtopic'),
    # ex: /agora/topics/5/newrep/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newrep$', views.new_rep, name='newrep'),
    # ex: /agora/topics/5/subs/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/subs/', views.subscribe_topic, name='subs'),
    # ex: /agora/topics/sankey/
    #url(r'^all_topics/sankey/', views.post_sankey, name='post_sankey'),
    # ex: /agora/topics/5/forcearrows/
    url(r'^all_topics/forcearrows/', views.topic_forcearrows, name='topic_forcearrows'),
    # ex: /agora/topics/5/forcearrows/
    url(r'^topics/(?P<topic_id>[0-9]+)/forcearrows/', views.topic_forcearrows, name='topic_forcearrows'),
    # ex: /agora/topics/new/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newpost/$', views.new_post, name='newpost'),
    # ex: /agora/topics/new/
    url(r'^topics/(?P<parent_topic_id>[0-9]+)/newpost/(?P<parent_post_id>[0-9]+)$', views.new_post, name='newpost'),
    # ex: /agora/topics/5/posts/5/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)/$', views.posts, name='posts'),
    # ex: /agora/topics/5/posts/5/vote/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)/vote/$', views.vote_post, name='vote_post'),
    # ex: /agora/topics/5/posts/5/newtag/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)/newtag/$', views.new_tag, name='newtag'),
    # ex: /agora/topics/5/posts/5/sankey/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)/sankey/$', views.post_sankey, name='post_sankey'),
    # ex: /agora/topics/5/posts/5/quickvote/
    url(r'^topics/(?P<topic_id>[0-9]+)/posts/(?P<post_id>[0-9]+)/quickvote/$', views.vote_post_quick, name='quickvote'),
    # ex: /agora/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]