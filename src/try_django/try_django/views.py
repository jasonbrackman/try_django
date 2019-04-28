from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    page_title = "Main Page"
    context = {
        "title": page_title,
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "home.html", context)


def about_page(request):
    page_title = "About us..."
    return render(request, "hello_world.html", {"title": page_title})


def contact_page(request):
    page_title = "Contact us ..."
    return render(request, "hello_world.html", {"title": page_title})


def example_page(request):
    page_title = "Example Page"
    context = {"title": page_title}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))

