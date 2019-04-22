from django.shortcuts import render


def home_page(request):
    page_title = "Home"
    return render(request, "home.html", {"page_title": page_title})
