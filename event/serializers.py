from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from .models import Event, EventType
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes the User instances"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class UserRegistrationSerializer(UserCreateSerializer):
    """Serializes a User registration form"""
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'email', 'password', 'is_staff')


class EventTypeSerializer(serializers.ModelSerializer):
    """Serializes the EventType instances"""
    class Meta:
        model = EventType
        fields = '__all__'


class ReadEventSerializer(serializers.ModelSerializer):
    """Serializes the Event instances for GET method"""
    creator = UserSerializer()
    type = EventTypeSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class WriteEventSerializer(serializers.ModelSerializer):
    """Serializes the Event instances for POST method"""
    creator = UserSerializer(required=False)
    type = serializers.CharField()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        title = validated_data.get('title')
        text = validated_data.get('text')
        creator = self.context.get('request').user
        spending_date_time = validated_data.get('spending_date_time')

        type_title = validated_data.get('type').lower()
        try:
            event_type = EventType.objects.get(title=type_title)
        except EventType.DoesNotExist:
            event_type = EventType.objects.create(title=type_title)

        event = Event.objects.create(
            title=title,
            text=text,
            creator=creator,
            type=event_type,
            spending_date_time=spending_date_time
        )
        return event
