from django.test import TestCase
from django.test import Client
from .models import PushModel

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def testPushView(self):
        response = self.client.post('/push/', {'push_message': 'test push view message', 'push_url': 'http://www.baidu.com'}, follow=True)
        self.assertTrue(len(response.redirect_chain) > 0)
        self.assertEqual(response.status_code, 200)

        self.pushmodel = PushModel.objects.get(push_message = 'test push view message')
        self.assertEqual(self.pushmodel.push_message, 'test push view message')
        self.assertEqual(self.pushmodel.push_url, 'http://www.baidu.com')
