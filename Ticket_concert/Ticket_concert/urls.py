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
from music.views import (Home, get_json_event, get_json_music,
                         get_json_album, Album_view,Album_list,
                         Music_list, Event_list,Event_view,
                         GD_signup,GD_signin, ApiEndpoint, 
                         GD_get_user_profile, GD_signout,
                         GD_Cart_add, GD_Cart,GD_Checkout_list,
                         GD_Checkout_confirm,GD_TransactionInfo,
                         GD_TransactionInfo_add,GD_Cart_edit,
                         GD_Cart_remove, GD_signup_check_exists, 
                         GD_Change_User_Picture)

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('',Home, name='home'),
    path('json/ticket/',get_json_event,name='get_json_ticket'),
    path('json/music/',get_json_music,name='get_json_music'),
    path('json/album/',get_json_album,name='get_json_album'),

    #album
    path('album/<int:pk>/', Album_view,name='album_view'),
    path('album/list/',Album_list,name='album_list'),

    #music
    path('music/list/',Music_list,name='music_list'),

    #event
    path('event/<int:pk>/',Event_view,name='event_view'),
    path('event/list/',Event_list,name='event_list'),

    #user's handler
    path('signup/',GD_signup,name='signup'),
    path('signup/check-exists/',GD_signup_check_exists),
    path('signin/',GD_signin,name='signin'),
    path('signout/',GD_signout,name='signout'),
    path('users/<str:username>/',GD_get_user_profile, name='user_profile'),
    path('profile/change_picture/',GD_Change_User_Picture),

    #oauth2
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/hello', ApiEndpoint.as_view()),

    #cart
    path('cart/add/',GD_Cart_add,name='add_cart'),
    path('cart/edit/',GD_Cart_edit,name='edit_cart'),
    path('cart/remove/',GD_Cart_remove,name='remove_cart'),
    path('cart/list/',GD_Cart,name='cart_list'),

    #transactions
    path('transactions/info/add/',GD_TransactionInfo_add,name='add_transaction'),
    path('transactions/info/',GD_TransactionInfo,name='info_transaction'),

    #checkout
    path('checkout/list/',GD_Checkout_list),
    path('checkout/confirm/',GD_Checkout_confirm),

    #============= Api Urls ============
    path('api/',include('api.urls'),name='api')
]