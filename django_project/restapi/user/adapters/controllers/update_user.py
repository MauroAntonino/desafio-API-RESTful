from django.http import HttpResponse
from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.infra.repository.mysql import MySql
from restapi.user.entities.objects.user import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from os import path
basedir = path.abspath(path.dirname(__file__))
uploads_path = path.join(basedir, 'static')

userService = UserService(user_repository=UserRepositoryAdapter(MySql))

@csrf_exempt
@api_view(["POST"])
def update_user(request):
    try:
        if request.method == 'POST':
            image = request.data.get('new_image')
            user = User(
                name=request.data.get("new_name"),
                password=request.data.get("new_password"),
                email=request.data.get("email"),
                user_id=None,
                image_url=None
            )
            if request.session.get('user',None) != None:
                user = userService.update_user(user=user, image=image)
                return JsonResponse(user, safe=False)
            else:
                return JsonResponse({"msg": "You are not logged in"})
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})