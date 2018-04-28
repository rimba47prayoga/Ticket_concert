from django.test import TestCase
from .models import Album, Music, Event, Cart, Transaction_info
from django.shortcuts import reverse
from django.core.paginator import Paginator
from oauth2_provider.models import AccessToken
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
class GreenDayTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='rimba47prayoga',password='123456')
        User.objects.create_user(username='rimba47',password='123456')
        album = Album.objects.create(nameapp='Revolutions Radio',release_date='2016-10-07',
                             genre='Punk rock, Punk pop, Rock alternatif',
                             descriptions='There\'s No Descriptions')
        music = Music.objects.create(nameapp='Stay The Night',durations='3:14',album=album)
        event = Event.objects.create(total_ticket=10000,
                                     ticket_date='2018-05-12T20:00:00',
                                     price=2000000,descriptions='No Descriptions')
        event.ticket_for.add(music)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_contains_album(self):
        response = self.client.get('/')
        album_context = response.context['album']
        album = Album.objects.get(idapp=1)
        self.assertEqual(album_context[0],album.get_dict())

    def test_home_contains_music(self):
        response = self.client.get('/')
        music_context = response.context['music']
        music = Music.objects.retrieveData()
        self.assertEqual(music_context[0],music[0])

        self.assertEqual(response.status_code,200)
    def test_album_absolute_url(self):
        album = Album.objects.get(idapp=1)
        self.assertEqual(album.get_absolute_url(),'/album/1/')

    def test_album_absolute_url_reverse(self):
        album = Album.objects.get(idapp=1)
        response = self.client.get(reverse('album_view',kwargs={'pk':album.idapp}))
        self.assertEqual(response.status_code,200)

    def test_album_contains_related_music_in_template(self):
        album = Album.objects.get(idapp=1)
        response = self.client.get(reverse('album_view',kwargs={'pk':album.idapp}))
        music = Music.objects.get(idapp=1)
        self.assertEqual(response.context['obj'],album)
        self.assertEqual(response.context['related_music'][0],music)

    def test_music_is_instance_paginator(self):
        music = Music.objects.all()
        response = self.client.get('/music/list/')
        self.assertIsInstance(response.context['music'].paginator,Paginator)

    def test_music_is_paginated(self):
        music = Music.objects.retrieveData()[0]
        response = self.client.get('/music/list/?page=1')
        music_context = response.context['music'].object_list[0]
        self.assertEqual(music,music_context)

    def test_can_login(self):
        response = self.client.login(username='rimba47prayoga',password='123456')
        self.assertEqual(response,True)

    def test_get_cart_is_must_login(self):
        response = self.client.get('/cart/list/')
        self.assertEqual(response.url,'/signin/?next=/cart/list/')

    def test_after_login_is_redirect(self):
        response = self.client.post('/signin/',{'username':'rimba47prayoga','password':'123456',
                                                'this_method_for_unit_test_only':'Icxj2TdNhfbwW5t0aR1h6l0BUDob90'})
        self.assertIsInstance(response,HttpResponseRedirect)

    def test_after_login_is_have_token(self):
        response = self.client.post('/signin/',{'username':'rimba47prayoga','password':'123456',
                                                'this_method_for_unit_test_only':'Icxj2TdNhfbwW5t0aR1h6l0BUDob90'})
        token = AccessToken.objects.filter(user=1).exists()
        self.assertEqual(token,True)

    def login_then_to_cart(self):
        response_login = self.client.post('/signin/',{'username':'rimba47prayoga','password':'123456',
                                                'this_method_for_unit_test_only':'Icxj2TdNhfbwW5t0aR1h6l0BUDob90',
                                                'next':'/cart/list/'})
        self.assertIsInstance(response_login,HttpResponseRedirect)
        redirect_after = response_login.url
        response_after_login = self.client.get(redirect_after)
        user = response_after_login.context['user'].id
        ticket = Event.objects.get(idapp=1)
        cart = Cart.objects.create(user=User.objects.get(id=user),
                                                  quantity=3,ticket=ticket)
        return (user,ticket,cart)

    def test_user_cart_is_filter_each_user(self):
        user, ticket, cart = self.login_then_to_cart()
        other_user = User.objects.get(id=2)
        other_user_cart = Cart.objects.create(user=other_user,quantity=2,ticket=ticket)
        response = self.client.get('/cart/list/')
        #check his cart
        self.assertIn(cart.get_dict(),response.context['cart'])
        #check if other user's cart not in his cart
        self.assertNotIn(other_user_cart.get_dict(),response.context['cart'])

    def test_after_user_add_ticket_to_cart_stock_ticket_not_decreased(self):
       user, ticket, cart =  self.login_then_to_cart()
       ticket_stock = ticket.total_ticket
       cart_quantity = cart.quantity
       self.assertNotEqual(ticket_stock,ticket_stock-cart_quantity)

    def test_info_address_is_his_user(self):
        user_id, ticket, cart =  self.login_then_to_cart()
        user = User.objects.get(id=user_id)
        transaction_info = Transaction_info.objects.create(user=user,no_telp='08953221545464',
                                                           province='Jawa Barat',code_pos='40512',
                                                           city='Cimahi',address='unknown')
        response = self.client.get('/checkout/confirm/')
        self.assertEqual(transaction_info.idapp,response.context['address'][0]['idapp'])

    #def test_stock_ticket_after_buy_is_decreased(self):
