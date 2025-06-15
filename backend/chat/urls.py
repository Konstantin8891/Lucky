from chat.views import MessageView
from django.urls import include, path

auth_app_urls = [
    path("messages/", MessageView.as_view(), name="register"),
]

app_prefix = [
    path("chat/", include(auth_app_urls)),
]


urlpatterns = [
    path("v1/", include(app_prefix)),
]