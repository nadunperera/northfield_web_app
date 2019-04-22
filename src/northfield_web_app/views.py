from django.shortcuts import render


def home_page(request):
    page_title = 'Property Expense Management System'
    template_name = 'home.html'
    context = {'page_title': page_title, 'home_link': 'active'}
    return render(request, template_name, context)
