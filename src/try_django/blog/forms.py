from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact="title")
        if self.instance is not None:
            qs.exclude(id=self.instance.id)
        if qs.exists():
            raise forms.ValidationError("This title is already used, please use another.")
        return title