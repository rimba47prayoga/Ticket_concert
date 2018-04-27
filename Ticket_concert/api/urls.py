from django.urls import path
from .views import MusicList, AlbumList, EventList, UserList,\
 CartList, TransactionList, Transaction_infoList, LoginView,LogoutView,RegisterView

urlpatterns = [
    path('music/list/',MusicList.as_view(),name='api_music_list'),
    path('album/list/',AlbumList.as_view(),name='api_album_list'),
    path('event/list/',EventList.as_view(),name='api_event_list'),
    path('user/list/',UserList.as_view(),name='api_user_list'),
    path('cart/list/',CartList.as_view(),name='api_user_list'),
    path('transaction/info/list/',Transaction_infoList.as_view(),name='api_transaction_info_list'),
    path('transaction/list/',TransactionList.as_view(),name='api_transaction_list'),
    path('login/',LoginView.as_view(),name='login_api'),
    path('logout/',LogoutView.as_view(),name='logout_api'),
    path('register/',RegisterView.as_view(),name='register_api')
    ]