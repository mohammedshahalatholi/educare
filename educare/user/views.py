from django.shortcuts import render

# Create your views here.
def U_Home(request):
    return render(request,"index.html")