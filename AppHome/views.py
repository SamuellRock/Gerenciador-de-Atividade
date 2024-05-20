from django.shortcuts import render

def dash_home(request):
    if request.method == 'GET':
        return render(request, 'navbar_base.html')