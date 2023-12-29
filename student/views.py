import json
from .models import StudentData
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        try:
            decoded_data = json.loads(request.body.decode('utf-8'))
            data = json.loads(request.body)
            s = StudentData.objects.create(id=data['id'], name=data['name'], age=data['age'], address=data['address'])
            # response = s.save()
            print(s)
            return JsonResponse(decoded_data)
        except Exception as e:
            return HttpResponse(f'<h2>Error: {e}</br></br>Please enter required fields.</h2>')

    else:
        return HttpResponse('<h2>Else block</h2>')


@csrf_exempt
def put_data(request):
    try:
        if request.method == 'PUT':
            pk = request.GET.get('id')
            decoded_data = json.loads(request.body.decode('utf-8'))
            StudentData.objects.filter(pk=pk).update(**decoded_data)
            return HttpResponse(f"<h2>Data updated successfully.</h2>")
    except Exception as e:
        return HttpResponse(f"<h2>Error: {e}</br></br>Data not Updated!!</h2>")

    return HttpResponse('<h2>Put method.</h2>')


def get_data(request):
    if request.method == 'GET':
        try:
            pk = request.GET.get('id')
            details = StudentData.objects.get(pk=pk)
            data = {'id': details.id, 'name': details.name, 'age': details.age, 'address': details.address}
            print(data)

            return JsonResponse(data)
        except Exception as e:
            return HttpResponse(f"<h2 style='font-family:Helvetica'>Error:{e}</br></br>No Data Found.</h2>")

    else:
        return HttpResponse("<h2 style='font-family:Helvetica'>No data found</h2>")
