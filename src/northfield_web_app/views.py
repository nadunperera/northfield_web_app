from django.shortcuts import render


def home_page(request):
    page_title = 'Home'
    home_link = 'active'
    template_name = 'home.html'
    context = {'page_title': page_title, 'home_link': home_link}
    return render(request, template_name, context)
