from django.shortcuts import render

# Create your views here.
def all_pizzas(request):
    return render(request, 'pages/index.html')
