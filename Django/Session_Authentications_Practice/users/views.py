from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method=='POST':
        data= json.loads(request.body)
        username= data.get('username')
        password= data.get('password')

        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message':'User Logged In!!'})
        else:
            return JsonResponse({'error': 'Invalid Credentials'}, status=400)


@csrf_exempt
def user_view(request):
    try:
        body= json.loads(request.body.decode("utf-16"))
    except:
        body= {}

    user= User.objects.first()

    if request.method =="GET":
        if user:
            return JsonResponse({
                "Username": user.username,
                "Passord": user.password
            })
        return JsonResponse({"Error": "No Such User Exists"}, status=404)

@csrf_exempt
def create_user(request):
    body = json.loads(request.body.decode("utf-8"))
    username= body.get("username")
    password= body.get("password")
    email=body.get("email")
    if request.method== "POST":
        if User.objects.filter(username= username):
            return JsonResponse({"error": "User already present"}, status=409)

        else:
            user= User.objects.create_user(username= username, password=password, email=email)
            return JsonResponse({"success": "User created successfully"}, status=200)