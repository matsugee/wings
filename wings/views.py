from django.shortcuts import render

def schedule_list(request):
    return render(request, 'wings/schedule_list.html', {})
