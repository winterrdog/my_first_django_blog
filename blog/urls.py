from django.urls import path
from . import views

# list of path converters that Django will try in order.
urlpatterns = [
    path("", views.post_list, name="post_list"),
]
