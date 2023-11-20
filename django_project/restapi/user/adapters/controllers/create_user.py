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
def create_user(request):
    try:
        if request.method == 'POST':
            image = request.data.get('image')
            user = User(
                name=request.data.get("name"),
                password=request.data.get("password"),
                email=request.data.get("email"),
                user_id=None,
                image_url=None
            )
            user = userService.create_user(user=user, image=image)
            return JsonResponse(user)
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})


@csrf_exempt
@api_view(["POST"])
def logout(request):
    try:
        del request.session['user']
    except:
        return JsonResponse({"msg": "already logged out"})
    return JsonResponse({"msg": "successfully logged out"})

@csrf_exempt
@api_view(["GET"])
def serve_image(request, id, email):
    try:
        path = uploads_path + "/" + id + "/" + email + ".jpeg"

        image_data = open(path, "rb").read()
        if image_data == None:
            return HttpResponse("File not Found")
        return HttpResponse(image_data, mimetype="image/jpeg")
    except:
        HttpResponse("File not Found")