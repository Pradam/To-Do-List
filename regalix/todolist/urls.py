from django.conf.urls import url
from .views import (ToDoWorkList, todo_new, todo_edit, todo_delete)

urlpatterns = [
    url(r'^$', ToDoWorkList.as_view()),
    url(r'^new/$', todo_new, name='todo_new'),
    url(r'^edit/(?P<pk>\d+)/$', todo_edit, name='todo_edit'),
    url(r'^delete/(?P<pk>\d+)/$', todo_delete, name='todo_delete'),
]
