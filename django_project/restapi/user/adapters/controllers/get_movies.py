from django.http import HttpResponse
from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.infra.repository.mysql import MySql
from restapi.user.entities.objects.movie import Movie
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from os import path
userService = UserService(user_repository=UserRepositoryAdapter(MySql))

@csrf_exempt
@api_view(["GET"])
def get_movies(request):
    try:
        if request.method == 'GET':
            page_size = request.GET.get("page_size", 3)
            page = request.GET.get("page", 0)
            search = request.GET.get("search", None)
            order = request.GET.get("order", None)
            if request.session.get('user',None) != None:
                movies_list = userService.get_movies(page_size=page_size, page=page, search=search, order=order)
                return JsonResponse(movies_list, safe=False)
            else:
                return JsonResponse({"msg": "You are not logged in"})
            
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})