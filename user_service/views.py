import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import user_details
from .serializers import UserDetailsSerializer

@csrf_exempt
def create(request):
    try:
        if request.method == "POST":  
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
           
            serializer = UserDetailsSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"User created successfully!!","data":serializer.data},status=201)
            else:
                return JsonResponse({"message":"Invalid Data Provided"})
        else:
            return JsonResponse({"message": "Invalid Http Method"},status=405)
    except Exception as error:
        return JsonResponse({"message":"Something went wrong","error":str(error)},status=500)


@csrf_exempt
def update(request, pk):
    try:
        user = user_details.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            serializer = UserDetailsSerializer(user, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "User updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except user_details.DoesNotExist:
        return JsonResponse({"message": "User not found!!!"}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)



@csrf_exempt
def get_details(request, pk):
    try:
        user = user_details.objects.get(pk=pk)
        serializer = UserDetailsSerializer(user)
        return JsonResponse(serializer.data)
    except user_details.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def delete_user(request, pk):
    try:
        user = user_details.objects.get(pk=pk)
        if request.method == 'DELETE':
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
    except user_details.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)



@csrf_exempt
def get_all_user_list(request):
    users = user_details.objects.all()
    serializer = UserDetailsSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
