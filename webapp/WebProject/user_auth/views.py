#importing Django libraries
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import re
import base64
import time

#--------------------------------------------------------------------------------
# Function definitions
#--------------------------------------------------------------------------------

#Validating passwords
def validatePassword(password):
	message =""
	specialCharacters = ['$', '#', '@', '!', '*','_','-','&','^','+','%']
	if(len(password)==0):
		return JsonResponse({'message':'Password can\'t be blank'})

	if (6>len(password) or len(password)>=12):
		message+= 'The password must be between 6 and 12 characters. : '
	password_strength = {}
	if not re.search(r'[A-Z]', password):
		message+= "Password must contain one upppercase : "
	if not re.search(r'[a-z]', password):
		message+= "Password must contain one lowercase : "

	if not re.search(r'[0-9]', password):
		message+= "Password must contain one numeric : "

	if not any(c in specialCharacters for c in password):
		message+= "Password must contain one special character : "
	
	if (len(message)>0):
		return JsonResponse({'message':message})
	else:
		return True

#Validing username
def validateUserName(username):
	valid = re.search(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$',username)
	if valid:
		return True
	return JsonResponse({'message': '"* please enter valid email ID *"'})


#--------------------------------------------------------------------------------
# Views definitions
#--------------------------------------------------------------------------------	
@csrf_exempt
def index(request):
	return HttpResponse("Hello")

@csrf_exempt
def registerPage(request):
	if request.method == 'POST':
		received_json_data = json.loads(request.body.decode("utf-8"))
		print(received_json_data)
		username = received_json_data['username']
		password = received_json_data['password']
		if (username==None or password == None):
			return JsonResponse({'message':'Username or password cant be empty'})
		username_status = validateUserName(username)
		password_status = validatePassword(password)
		if (username_status == True and password_status == True):
			email = username
			if not User.objects.filter(username=username).exists():
				user = User.objects.create_user(username, email, password)
				print("User Details :" + str(user))
				user.is_staff= True
				user.save()
				return JsonResponse({"message" : "user created"})
			else:
				return JsonResponse({'Error' :  username + ' already exists'})
		else:
			if(password_status == True):
				return JsonResponse({"message" : username_status})	
			elif (username_status == True):
				return JsonResponse({"message" : password_status})
			else:
				return JsonResponse({'message':username_status + " " + password_status})
	return JsonResponse({'message':'Error : Please use a post method with parameters username and password to create user'})

def testpage(request):
    return HttpResponse("testpage" + password_check("testa"))

def signin(request):
	if 'HTTP_AUTHORIZATION' in request.META:
		auth = request.META['HTTP_AUTHORIZATION'].split()
		if len(auth) == 2:
			if auth[0].lower() == "basic":
				authstring = base64.b64decode(auth[1]).decode("utf-8")
				username, password = authstring.split(':', 1)
				if not username and not password:
					return JsonResponse({'message':'Error : User not logged, Please provide credentials'}, status=401)
				user = authenticate(username=username, password=password)
				if user is not None and user.is_staff:
				# handle your view here
					return JsonResponse({"current time": time.ctime()})
	# otherwise ask for authentification
	return JsonResponse({'message': 'Error : Incorrect user details'}, status=401)