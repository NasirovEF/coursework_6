from django.urls import path

from coursework.apps import CourseworkConfig
from coursework.views import FirstPageView, ClientListView, ClientUpdateView, ClientDeleteView, ClientCreateView, \
    MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = CourseworkConfig.name

urlpatterns = [
    path('', FirstPageView.as_view(), name='first_page'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
]
