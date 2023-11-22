from django.http import HttpResponse
from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.adapters.email.user_email_adapter import UserEmailAdapter
from restapi.user.infra.repository.mysql import MySql
from restapi.user.entities.objects.user import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os import path
import logging
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')
logger = logging.getLogger(__name__)

userService = UserService(user_repository=UserRepositoryAdapter(MySql), user_email=UserEmailAdapter(MySql))

@csrf_exempt
@api_view(["POST"])
def create_user(request):
    try:
        if request.method == 'POST':
            image = request.data.get('image')
            user = User(
                name=request.data.get("name"),
                password=request.data.get("password"),
                email=request.data.get("email"),
                user_id=None,
                image_url=None,
                is_confirmed=False
            )
            user = userService.create_user(user=user, image=image)
            return JsonResponse(user)
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})

@csrf_exempt
@api_view(["GET"])
def serve_image(request, id):
    try:
        logger.info(id)
        fs = FileSystemStorage(location=settings.STATIC_ROOT)
        with open(fs.path(id), 'rb') as image_file:
            image_bytes = image_file.read()
        return HttpResponse(image_bytes, content_type=f'image/jpeg')
    except Exception as ex:
        logger.info(ex)
        return HttpResponse("File not Found")