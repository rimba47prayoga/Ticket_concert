from django.db import models
# Create your models here.
from django.urls import reverse
from datetime import date
from .data_layer.Music_BR import Music_BR_Manager
class Album(models.Model):
    idapp = models.AutoField(primary_key=True)
    nameapp = models.CharField(max_length=125)
    release_date = models.DateField()
    genre = models.CharField(max_length=250,null=True)
    picture = models.ImageField(null=True)
    descriptions = models.TextField(null=True)

    def __str__(self):
        return self.nameapp

    def get_absolute_url(self):
        return reverse('album_view',kwargs={'pk':self.idapp})

    def get_dict(self):
        return {'link_url':self.get_absolute_url(),'nameapp':self.nameapp,
                'picture':self.picture.name,
                'descriptions':self.descriptions[:70] + '...'}

class Music(models.Model):
    idapp = models.AutoField(primary_key=True)
    nameapp = models.CharField(max_length=150)
    durations = models.CharField(max_length=4, null=True)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameapp
    objects = Music_BR_Manager()

class Event(models.Model):
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

    def get_absolute_url(self):
        return reverse('event_view',kwargs={'pk':self.idapp})

    def get_dict_event(self,user=None):
        music_list = self.ticket_for.all()
        count_music = music_list.count()
        music = music_list[0].nameapp
        if count_music > 1:
            music = ','.join(i.nameapp for i in music_list)
        location = self.location
        sub_location = ''
        if ',' in location:
            location = location.split(',')[0]
            sub_location = self.location.split(',')[1:][0]
        q_sold = self.ticket_transaction_set.values('quantity')
        total_sold = 0
        for i in q_sold:
            total_sold += i['quantity']
        data = {'idapp':self.idapp,'music_list':music,'location':location,
                'sub_location':sub_location,
                'ticket_date':self.ticket_date,
                'price':self.price,'descriptions':self.descriptions,
                'available_ticket':self.total_ticket,
                'total_sold':total_sold,
                'total_ticket': self.total_ticket + total_sold,
                'link_url':self.get_absolute_url()}
        if user is not None:
            is_add = self.cart_set.filter(user=user).exists()
            if is_add:
                data['is_add'] = True
            else:
                data['is_add'] = False
        return data

    #def get_stock_ticket(self):


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='User_image/',default='User_image/User-Default.jpg')

class Transaction_info(models.Model):
    idapp = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    no_telp = models.CharField(max_length=15,null=True)
    province = models.CharField(max_length=50,null=True) #provinsi
    code_pos = models.CharField(max_length=10,null=True) 
    city = models.CharField(max_length=20,null=True) #kota
    address = models.TextField(null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)

class Ticket_transaction(models.Model):
    idapp = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    ticket = models.ForeignKey(Event,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    createddate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    

    #def get_checkout_info(self):
    #    ticket = self.ticket
    #    return {
    #        'idapp':self.idapp,
    #        'location':ticket.location,
    #        'ticket_date':ticket.ticket_date,
    #        'quantity':self.quantity,
    #        'price':str(ticket.price),
    #        'total_price':str(self.quantity*ticket.price)
    #        }

class Cart(models.Model):
    idapp = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ticket = models.ForeignKey(Event,on_delete=models.CASCADE, null=True)

    def get_dict(self):
        ticket = self.ticket
        location = ticket.location
        sub_location = ''
        if ',' in location:
            location = location.split(',')[0]
            sub_location = self.ticket.location.split(',')[1:][0]
        return {
            'idapp':self.idapp,
            'location':location,
            'sub_location':sub_location,
            'ticket_date':ticket.ticket_date,
            'quantity':self.quantity,
            'price':str(ticket.price),
            'total_price':str(self.quantity*ticket.price),
            'descriptions':ticket.descriptions
            }
    def get_checkout_info(self):
        ticket = self.ticket
        return {
            'idapp':self.idapp,
            'idapp_ticket':self.ticket.idapp,
            'location':ticket.location,
            'ticket_date':ticket.ticket_date,
            'quantity':self.quantity,
            'price':str(ticket.price),
            'total_price':str(self.quantity*ticket.price)
            }