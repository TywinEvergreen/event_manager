from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from django.utils import timezone

from .models import Event, EventType

from .serializers import ReadEventSerializer, WriteEventSerializer, EventTypeSerializer
from .permissions import IsCreatorOrReadOnly, IsAdminOrReadOnly


class EventListCreateAPIView(ListCreateAPIView):
    """Provides GET/POST methods for events/"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Filters Event instances by title and date"""
        title_filter = self.request.query_params.get('title_filter')
        date_filter = self.request.query_params.get('date_filter')

        if title_filter:
            queryset = Event.objects.filter(title__icontains=title_filter)
        else:
            queryset = Event.objects.all()

        if date_filter == 'month':
            return queryset.filter(date_time_created__gte=timezone.now() - timezone.timedelta(days=30))
        elif date_filter == 'week':
            return queryset.filter(date_time_created__gte=timezone.now() - timezone.timedelta(days=7))
        elif date_filter == 'day':
            return queryset.filter(date_time_created__date=timezone.now().date())
        else:
            return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteEventSerializer
        else:
            return ReadEventSerializer


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Provides GET/PUT/PATCH/DELETE methods for events/<slug>"""
    queryset = Event.objects.all()
    lookup_field = 'slug'
    serializer_class = ReadEventSerializer
    permission_classes = [IsCreatorOrReadOnly]


class EventTypeListCreateAPIView(ListCreateAPIView):
    """Provides GET/POST methods for types/"""
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EventTypeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """Provides GET/DELETE methods for type/<title>"""
    queryset = EventType.objects.all()
    lookup_field = 'title'
    serializer_class = EventTypeSerializer
    permission_classes = [IsAdminOrReadOnly]
