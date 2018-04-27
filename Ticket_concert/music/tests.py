from django.test import TestCase
from .models import Album, Music
from django.shortcuts import reverse
from django.core.paginator import Paginator
from oauth2_provider.models import AccessToken
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class GreenDayTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='rimba47prayoga',password='123456')
        album = Album.objects.create(nameapp='Revolutions Radio',release_date='2016-10-07',
                             genre='Punk rock, Punk pop, Rock alternatif',
                             descriptions='There\'s No Descriptions')
        music = Music.objects.create(nameapp='Stay The Night',durations='3:14',album=album)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    def test_home(self):
        response = self.client.get('/')

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

    #def test_stock_ticket_after_buy_is_decreased(self):
