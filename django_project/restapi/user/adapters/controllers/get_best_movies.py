from restapi.user.usecases.user_service import UserService
from restapi.user.adapters.repository.user_repository_adapter import UserRepositoryAdapter
from restapi.user.adapters.email.user_email_adapter import UserEmailAdapter
from restapi.user.infra.repository.mysql import MySql
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from os import path
userService = UserService(user_repository=UserRepositoryAdapter(MySql), user_email=UserEmailAdapter(MySql))

@csrf_exempt
@api_view(["GET"])
def get_best_movies(request):
    try:
        if request.method == 'GET':
            page_size = request.GET.get("page_size", 3)
            page = request.GET.get("page", 0)
            search = request.GET.get("search", None)
            order = request.GET.get("order", None)
            email = request.GET.get("email", None)
            if request.session.get('user',None) != None:
                movies_list = userService.get_best_movies(page_size=page_size, page=page, search=search, order=order, email=email)
                return JsonResponse(movies_list, safe=False)
            else:
                return JsonResponse({"msg": "You are not logged in"})
            
    except Exception as ex: 
        print(ex)
        return JsonResponse({"msg": str(ex)})