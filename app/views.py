from django.shortcuts import render

# Create your views here.
def dev(request):
    return render(request,'dev.html')

def devika(request):
    return render(request,'devika.html')