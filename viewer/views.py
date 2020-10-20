from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from viewer.models import Data


def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def send_training(request):
    if request.method == 'POST':
        d = Data(loss=request.POST['loss'], tr_acc=request.POST['tr_acc'], val_acc=request.POST['val_acc'])
        d.save()
        return HttpResponse()
    else:
        return HttpResponse('Wrong method')

def get_training(request):
    d = Data.objects.all()

    result = []
    for i in d:
        result.append({'loss':i.loss, 'tr_acc':i.tr_acc, 'val_acc':i.val_acc})

    # return JsonResponse({'loss': loss, 'acc': acc})
    context = {'result':result}
    return render(request, 'viewer/training_results.html', context)

def del_everything(request):
    Data.objects.all().delete()

    return HttpResponse()