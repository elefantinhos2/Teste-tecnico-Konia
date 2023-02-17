from django.urls import path

from . import views

urlpatterns = [
    path("item/",views.ListCreateitemView.as_view()),
    path("item/<str:id_item>", views.DeleteItemView.as_view())
]
