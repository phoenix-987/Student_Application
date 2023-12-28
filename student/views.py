from .models import StudentData
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def delete_data(request):
    if request.method == 'DELETE':
        try:
            pk = request.GET.get('id')
            res = StudentData.objects.filter(pk=pk).delete()
            if res[0] == 1:
                return HttpResponse('<h1>Data Deleted successfully.</h1>')
            else:
                return HttpResponse('<h1>Data does not exist!</h1>')
        except Exception as e:
            return HttpResponse(f'<h1>Error: {e}</br></br>Unable to delete data!!</h1>')

    return HttpResponse('<h1>Delete Page.</h1>')
