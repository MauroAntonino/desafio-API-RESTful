from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.adapters.email.user_email_adapter import UserEmailAdapter
from restapi.user.infra.repository.mysql import MySql
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from os import path
import logging
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')
logger = logging.getLogger(__name__)

userService = UserService(user_repository=UserRepositoryAdapter(MySql), user_email=UserEmailAdapter(MySql))

@csrf_exempt
@api_view(["POST"])
def validate_email(request):
    try:
        if request.method == 'POST':
            email=request.POST['email']
            userService.send_token(email=email)
            return JsonResponse({"msg": "validation token sent to: {email}".format(email=email)})
    except Exception as ex: 
        logger.error(ex)
        return JsonResponse({"msg": str(ex)})

@csrf_exempt
@api_view(["POST"])
def confirm_token(request):
    try:
        if request.method == 'POST':
            email=request.POST['email']
            token=request.POST['token']
            userService.confirm_email(user_email=email, token=token)
            return JsonResponse({"msg": "Token is valid!"})
    except Exception as ex: 
        logger.error(ex)
        return JsonResponse({"msg": str(ex)})