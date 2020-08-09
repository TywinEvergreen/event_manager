from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, \
    EventTypeListCreateAPIView, EventTypeRetrieveDestroyAPIView, TestView

urlpatterns = [
    path('', EventListCreateAPIView.as_view()),
    path('<slug>', EventRetrieveUpdateDestroyAPIView.as_view()),
    path('types/', EventTypeListCreateAPIView.as_view()),
    path('types/<title>', EventTypeRetrieveDestroyAPIView.as_view()),
    path('test_view/', TestView.as_view())
]
