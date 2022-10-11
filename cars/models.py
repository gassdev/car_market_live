from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

year_choice = tuple((x,x) for x in range(2000, datetime.now().year+1))

features_choices = (
    ('Cruise Control', 'Cruise Control'),
    ('Audio Interface', 'Audio Interface'),
    ('Air conditioning', 'Air conditioning'),
    ('Seat Heating', 'Seat Heating'),
    ('Alarm System', 'Alarm System'),
    ('ParkAssist', 'ParkAssist'),
    ('Power Steering', 'Power Steering'),
    ('Reversing Camera', 'Reversing Camera'),
    ('Direct Fuel Injection', 'Direct Fuel Injection'),
    ('Auto Start/Stop', 'Auto Start/Stop'),
    ('Wind Deflector', 'Wind Deflector'),
    ('Bluetooth Handset', 'Bluetooth Handset'),
)

class Car(models.Model):
    car_title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    speed = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(('year'), choices=year_choice)
    price = models.PositiveIntegerField()
    condition = models.CharField(max_length=100)
    description = RichTextField()
    photo = models.ImageField(upload_to='photos/cars/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/cars/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/cars/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/cars/%Y/%m/%d', blank=True)
    engine = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    features = MultiSelectField(max_length=100, choices=features_choices, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.car_title