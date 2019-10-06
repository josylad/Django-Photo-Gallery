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


