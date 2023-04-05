from django.shortcuts import render
from .models import measurements
from django.shortcuts import render
from .models import measurements
from django.shortcuts import render
from .models import measurements

title = "Analytics Display"

def measurements_view(request):
    farms = measurements.objects.all()
    if request.method == 'POST':
        farm_id = request.POST.get('farm_id')
        date = request.POST.get('date')
        Measurements = measurements.objects.filter(farm=farm_id, date=date)
        return render(request, 'analytics/blank.html', {'measurements': Measurements, 'farms': farms, 'title': title, 'date': date})
    else:
        return render(request, 'analytics/blank.html', {'farms': farms, 'title': title})


