from django.shortcuts import (
    render,
    get_object_or_404,
)

# Create your views here.
from .models import BlogPost


def blog_post_list_view(request):
    # could list out or search for objects

    qs = BlogPost.objects.all()
    template_name = "blog_post_list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create a blog post using a form
    template_name = "blog_post_create.html"
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    # query_set = BlogPost.objects.filter(slug=slug)
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_delete.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)