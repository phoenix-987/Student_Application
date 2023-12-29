from .models import StudentData
from django.http import JsonResponse
from django.shortcuts import HttpResponse

# Create your views here.
STUDENT = StudentData()


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
