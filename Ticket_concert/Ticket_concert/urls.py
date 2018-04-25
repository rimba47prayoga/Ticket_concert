"""Ticket_concert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music.views import Home, get_json_event, get_json_music, \
    get_json_album, Album_view,Album_list,Music_list, Event_list,\
    Event_view,signup,signin, ApiEndpoint, get_user_profile, signout,\
    add_cart,GD_Transaction, GD_Cart,GD_Checkout_list,GD_Checkout_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('json/ticket/',get_json_event,name='get_json_ticket'),
    path('json/music/',get_json_music,name='get_json_music'),
    path('json/album/',get_json_album,name='get_json_album'),
    path('album/<int:pk>/', Album_view,name='album_view'),
    path('album/list/',Album_list,name='album_list'),
    path('music/list/',Music_list,name='music_list'),
    path('event/<int:pk>/',Event_view,name='event_view'),
    path('event/list/',Event_list,name='event_list'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/<str:username>/',get_user_profile),
    path('api/hello', ApiEndpoint.as_view()),  # an example resource endpoint

    path('add_to_cart/',add_cart,name='add_cart'),
    path('transactions/add/',GD_Transaction,name='add_transaction'),
    path('cart/list/',GD_Cart,name='cart_list'),

    path('checkout/list/',GD_Checkout_list),
    path('checkout/confirm/',GD_Checkout_confirm)
]