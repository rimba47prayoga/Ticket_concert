from django.db import models
# Create your models here.
from django.urls import reverse
from .data_layer.Music_BR import Music_BR_Manager
class Album(models.Model):
    idapp = models.AutoField(primary_key=True)
    nameapp = models.CharField(max_length=125)
    picture = models.ImageField(null=True)
    descriptions = models.TextField(null=True)

    def __str__(self):
        return self.nameapp

    def get_absolute_url(self):
        return reverse('album_view',kwargs={'pk':self.idapp})

class Music(models.Model):
    idapp = models.AutoField(primary_key=True)
    nameapp = models.CharField(max_length=150)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameapp
    objects = Music_BR_Manager()

class Ticket(models.Model):
    idapp = models.AutoField(primary_key=True)
    ticket_for = models.ManyToManyField(Music)
    total_ticket = models.IntegerField()
    ticket_date = models.DateTimeField()
    location = models.CharField(max_length=120,default='Jakarta')
    price = models.DecimalField(max_digits=30,decimal_places=2)
    descriptions = models.CharField(max_length=250)

    def __str__(self):
        music_list = [i.nameapp for i in self.ticket_for.all()]
        str_music_list = ','.join(music_list)
        return 'Green Day - {0} ({1})'.format(self.location,str_music_list)
    def get_dict_ticket(self):
        music_list = self.ticket_for.all()
        count_music = music_list.count()
        music = music_list[0].nameapp
        if count_music > 1:
            music = ','.join(i.nameapp for i in music_list)
        return {'music_list':music,'location':self.location,
                'ticket_date':self.ticket_date.strftime('%d %B %Y %H:%M:%S'),
                'price':self.price,'descriptions':self.descriptions}