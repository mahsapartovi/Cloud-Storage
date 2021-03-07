from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import forms

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return JsonResponse({"upload file": "post /user/upload/  field_name=file", "show your file": "GET /user/myfiles/"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload(request):
    if request.method == 'POST':
        form = forms.UserFile(request.POST, request.FILES)
        if form.is_valid():
            models.UserFiles(user=request.user, file=form.cleaned_data["file"], file_size=form.cleaned_data["file"].size).save()
            return JsonResponse({"status": "ok"}, status=200)
    else:
        return JsonResponse({"status": "fail", "error": "just post request"}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fileList(request):
    files = models.UserFiles.objects.filter(user=request.user)
    sel = serializers.FileAPI(list(files), many=True)
    return JsonResponse(sel.data, status=200, safe=False)
