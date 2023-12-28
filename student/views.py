import json

from .models import StudentData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse


# Create your views here.
STUDENT = StudentData()


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
