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

import requests

@csrf_exempt
def get_vehicle_by_id(request):
    try:
        user_id = request.GET.get('user_id')  
        if user_id:
            print(user_id)
            user_object = user_details.objects.filter(user_id=user_id, is_deleted=False)
            user = user_details.objects.get(user_id=user_id, is_deleted=False)
            print

            serializer = UserDetailsSerializer(user)
            print(serializer.data)
            
            if user_object.exists:
                print("st")
              
                vehicle_response = requests.get("http://127.0.0.1:8001/api/vehicle_details/get_vehicle_by_id",params={'user_id':user_id})
                print("sfdfs")
                print(user_id)
                print(vehicle_response)
                if vehicle_response.status_code==200:
                    vehicle_data=vehicle_response.json().get('data',())
                else:
                    print(vehicle_response)
                    vehicle_data=[]    

                data = {
                    "user_details":serializer.data,
                    "vehicle_details":vehicle_data
                }
                return JsonResponse({"message": f"User details for {user_id} retrieved successfully!!", "data": data})
            else:
                return JsonResponse({"message": f"No vehicle details found for {user_id}"})
        else:
            return JsonResponse({"message": "Date parameter is missing."}, status=400)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    