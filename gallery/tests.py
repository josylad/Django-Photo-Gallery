from django.test import TestCase
from .models import Category, Image, Location
# Create your tests here.

class CategoryTestCase(TestCase):
    
    def setUp(self):
        self.category = Category(category = 'Animals')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
        
    def test_save_categories(self):
        self.category.save_category()
        all_categories = Category.objects.all()
        self.assertTrue(len(all_categories) > 0)
        
    def test_search_category(self):
        self.category.save_category()
        images = Category.objects.filter(category__icontains='animals')
        self.assertTrue(self.category, images)
        
        

class LocationTestCase(TestCase):
    
    def setUp(self):
        self.location = Location(location = 'Lagos')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
        
    def test_save_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
    def test_get_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
        
