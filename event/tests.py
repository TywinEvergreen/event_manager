from rest_framework.test import APITestCase
from django.utils import timezone
from django.template.defaultfilters import slugify
from rest_framework import status

from .models import Event, EventType


class CustomTestCase(APITestCase):

    def setUp(self):
        token = self.create_api_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def create_api_user(self, username='username', email='email@gmail.com', is_staff=True):
        """Creates a User instance using API"""
        self.client.post('/auth/users/', {
            'username': username,
            'email': email,
            'password': 'test_password',
            'is_staff': is_staff
        })
        auth_response = self.client.post('/auth/token/login/', {
            'username': username,
            'password': 'test_password'
        })
        return auth_response.data['auth_token']

    def create_event(self, title='title'):
        """Creates an Event instance using API"""
        response = self.client.post('/events/', {
            'title': title,
            'text': 'text',
            'type': 'call',
            'spending_date_time': timezone.now()
        })
        return response.data


class EventTest(CustomTestCase):

    def test_create_event(self):
        self.create_event()
        self.assertEqual(Event.objects.count(), 1)

    def test_save_slug(self):
        event = self.create_event()
        self.assertEqual(event['slug'], slugify('title by username on {}'.format(timezone.now().date())))

    def test_filtering_by_date(self):
        self.create_event()
        for date_filter in ['month', 'week', 'day', '']:
            response = self.client.get('/events/', {
                'date_filter': date_filter
            })
            self.assertEqual(response.data['count'], 1)

    def test_filtering_by_title(self):
        self.create_event('title1')
        self.create_event('title2')
        response = self.client.get('/events/', {
            'title_filter': 'title2'
        })
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'title2')

    def test_retrieve_event_by_slug(self):
        event = self.create_event()
        response = self.client.get('/events/{}'.format(event['slug']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        event = self.create_event()
        response = self.client.patch('/events/{}'.format(event['slug']), {
            'text': 'alted text'
        })
        self.assertEqual(response.data['text'], 'alted text')

    def test_destroy_event(self):
        event = self.create_event()
        response = self.client.delete('/events/{}'.format(event['slug']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_alphanumeric_validation(self):
        response = self.create_event('!@#$%')
        self.assertEqual(response['title'][0], 'Only alphanumeric characters are allowed.')


class EventTypeTest(CustomTestCase):

    def test_create_event_type(self):
        EventType.objects.create(title='event_type')
        self.assertEqual(EventType.objects.count(), 1)

    def test_api_create_event_type(self):
        self.client.post('/events/types/', {'title': 'event_type'})
        self.assertEqual(EventType.objects.count(), 1)

    def test_retrieve_event_type_by_title(self):
        EventType.objects.create(title='event_type')
        response = self.client.get('/events/types/event_type')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_event_type(self):
        EventType.objects.create(title='event_type')
        response = self.client.delete('/events/types/event_type')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PermissionTest(CustomTestCase):

    def test_is_creator_or_read_only_permission(self):
        event = self.create_event()
        token = self.create_api_user('username2', 'email2@gmail.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch('/events/{}'.format(event['slug']))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_is_admin_or_read_only_permission(self):
        event = self.create_event()
        token = self.create_api_user('username2', 'email2@gmail.com', False)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.patch('/events/{}'.format(event['slug']))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
