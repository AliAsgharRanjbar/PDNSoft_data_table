from django.shortcuts import render, HttpResponse

# Create your views here.


def aboutme(request):
    return render(request, "test.html", {})



def handler404(request, *args, **argv):
    response = render(request,'404.html', {})
    response.status_code = 404
    return response


def home(request):
    return render(request, "home.html")