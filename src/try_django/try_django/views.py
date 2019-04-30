from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


def home_view(request):
    page_title = "Main Page"
    context = {
        "title": page_title,
        "my_list": [1, 2, 3, 4, 5],
    }
    return render(request, "home.html", context)


def about_view(request):
    page_title = "About us..."
    return render(request, "hello_world.html", {"title": page_title})


def contact_view(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()  # will clear out the form

    context = {
        "title": "Contact us ...",
        "form": form,
    }
    return render(request, "form.html", context)


def example_view(request):
    page_title = "Example Page"
    context = {"title": page_title}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))

