from django.shortcuts import render

# Create your views here.
def index(request):
    example = "hello"
    context = {
        'example': example
    }
    return render(request, "railway/index.html", context)