import json
from .models import StudentData
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
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
