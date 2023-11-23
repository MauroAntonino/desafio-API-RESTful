from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.adapters.email.user_email_adapter import UserEmailAdapter
from restapi.user.infra.repository.mysql import MySql
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)

userService = UserService(user_repository=UserRepositoryAdapter(MySql), user_email=UserEmailAdapter(MySql))

@csrf_exempt
@api_view(["POST"])
def login(request):
    try:
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')

            check_user = userService.auth_user(email=email, password=password)
            if check_user:
                request.session['user'] = email
                return JsonResponse({"msg": "login successfully"})
            else:
                return JsonResponse({"msg": "Please enter valid email or password."})
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})