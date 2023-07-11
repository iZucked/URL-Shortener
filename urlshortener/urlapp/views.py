from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import URL


# Create your views here.

def home(request):
    print(request.headers['User-Agent'])
    print(request.META)
    return render(request, "index.html", {'user': request.user})


def create_link(request):
    if request.POST:
        form = UrlForm(request.POST)
        form.save()

        print(form)
    else:
        return render(request, "create_link.html", {'form': UrlForm()})

def view_link(request, short_code):
    # Lookup short_code in url database
    url = URL.objects.get(shortened_code=short_code)

    # Create visitor

    # Redirect
    return redirect(url.linked_url)