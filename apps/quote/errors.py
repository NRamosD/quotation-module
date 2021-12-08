from django.shortcuts import render

def error_400(request, exception):
        data = {}
        return render(request,'./quote/html/errors/400.html', data)

def error_403(request, exception):
    data = {}
    return render(request,'./quote/html/errors/403.html' ,data)

def error_404(request, exception):
        data = {}
        return render(request,'./quote/html/errors/400.html', data)

def error_500(request):
        data = {}
        return render(request,'./quote/html/errors/500.html', data)

