from django.http import JsonResponse

#created the view
def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})

