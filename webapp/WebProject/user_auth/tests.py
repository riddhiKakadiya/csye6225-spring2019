from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
import base64
from .views import validateUserName 

class BasicAuthTest(TestCase):
	#creating user
	def setUp(self):
		print(validateUserName('rk@gmail.com'))
		self.username = 'rk@gmail.com'
		self.password = 'Riddhi@2911'
		self.user1 = User.objects.create_user(self.username, self.username, self.password)

	#testing root URL with basic auth
	def test_base_url(self):
		up = self.username+':'+self.password
		auth_headers = {'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(up.encode('utf-8')).decode('utf-8'),}
		c = Client()
		response = c.get('', **auth_headers)
		self.assertEqual(response.status_code, 200)	

	#deleting user
	def tearDown(self):
		self.user1.delete() 

	def testUserNameTrue(self):
		self.assertEqual(validateUserName('riddhikakadiya29@gmail.com'), True)
						
	def testUserNameFalse(self):
		self.assertEqual(validateUserName('riddhikakadiya29'), '* please enter valid email ID *')