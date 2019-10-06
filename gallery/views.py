from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Location, Image, Category
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def index(request):
    date = dt.date.today()
    images = Image.get_images()
    location = Location.get_location()
    locations = Location.get_location()

    return render(request, 'index.html', {"date": date, "images":images, "location":location, "locations":locations})


def search_images(request):
    locations = Location.get_location()
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_images = Image.search_by_categ(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images": searched_images, "locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message, "locations":locations})


def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return render(request, "images.html", {"image":image, "locations":locations})
    
    
