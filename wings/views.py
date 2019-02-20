   
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Schedule
from .forms import ScheduleForm

def schedule_list(request):
    schedules = Schedule.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'wings/schedule_list.html', {'schedules':schedules})

def schedule_detail(request, pk):
    sc = get_object_or_404(Schedule, pk=pk)
    return render(request, 'wings/schedule_detail.html', {'sc': sc})

def schedule_new(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.save()
            return redirect('schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'wings/schedule_edit.html', {'form': form})

def schedule_edit(request, pk):
    sc = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=sc)
        if form.is_valid():
            sc = form.save(commit=False)
            sc.save()
            return redirect('schedule_detail', pk=sc.pk)
    else:
        form = ScheduleForm(instance=sc)
    return render(request, 'wings/schedule_edit.html', {'form': form})

