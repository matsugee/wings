   
from django.shortcuts import render
from django.utils import timezone
from .models import Schedule

def schedule_list(request):
    schedules = Schedule.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'wings/schedule_list.html', {'schedules':schedules})
