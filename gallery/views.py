from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Location, Image, Category
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

