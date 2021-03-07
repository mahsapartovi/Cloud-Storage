from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from files import serializers

def index(request):
    return JsonResponse({"register" : "POST /register/  data => username, password", "login": "base auth", "dashbord": "/user/"})

@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = serializers.UserAPI(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"error": "just post request"})


