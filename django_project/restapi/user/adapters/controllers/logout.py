from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.adapters.email.user_email_adapter import UserEmailAdapter
from restapi.user.infra.repository.mysql import MySql
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from os import path
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')

userService = UserService(user_repository=UserRepositoryAdapter(MySql), user_email=UserEmailAdapter(MySql))

@csrf_exempt
@api_view(["POST"])
def logout(request):
    try:
        del request.session['user']
    except:
        return JsonResponse({"msg": "already logged out"})
    return JsonResponse({"msg": "successfully logged out"})