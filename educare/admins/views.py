from django.shortcuts import render

# Create your views here.
def A_Home(request):
    return render(request,"A_index.html")