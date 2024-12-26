from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "records/index.html")




def register(request):
    return render(request, "records/register.html")


def about(request):
    return render(request, "records/about.html")