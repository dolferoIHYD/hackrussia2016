from django.shortcuts import render
from django.http import HttpResponse

from tracker.models import Truck, Arrival, Deport

def monitor(request):
    if request.method == 'POST':
        if request.POST.get('number'):
            try:
                truck = Truck.objects.get(state_number=request.POST['number'])
            except Truck.DoesNotExist:
                return HttpResponse('Not found')
            arrivals = Arrival.objects.filter(truck = truck)
            deports = Deport.objects.filter(truck = truck)
        elif request.POST.get('name'):
            try:
                truck = Truck.objects.get(driver=request.POST['name'])
            except Truck.DoesNotExist:
                return HttpResponse('Not found')
            arrivals = Arrival.objects.filter(truck = truck)
            deports = Deport.objects.filter(truck = truck)
        elif request.POST.get('year'):
            arrivals = Arrival.objects.filter(date__year = request.POST['year'],
                                          date__month = request.POST['month'],
                                          date__day = request.POST['day'])
            deports = Deport.objects.filter(date__year = request.POST['year'],
                                          date__month = request.POST['month'],
                                          date__day = request.POST['day'])



        return render(request, 'arr-dep.html', {
            'arrivals': arrivals,
            'deports': deports,
        })

    elif request.method == 'GET':
        return render(request, 'base.html', {})
