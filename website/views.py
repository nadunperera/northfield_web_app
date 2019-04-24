from django.shortcuts import render


# Create your views here.
def home(request):
    template_name = 'website/home.html'
    context = {'home_link': 'active'}
    return render(request, template_name, context)
