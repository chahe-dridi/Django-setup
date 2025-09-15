from django.db import models
from django.core.validators import RegexValidator

category_list = [
    ('Musique', 'Musique'),
    ('Cinema', 'Cinema'),
    ('Sport', 'Sport'),
]



class Event(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    category = models.CharField(choices=category_list, max_length=30 )
    state = models.BooleanField(default=True)
   
    nbe_participant = models.IntegerField(default=0)
    evt_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title
