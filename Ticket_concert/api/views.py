from rest_framework import generics,status
from music.models import Music,Album, Event, Cart, Ticket_transaction, Transaction_info
from .serializers import MusicSerializer, AlbumSerializer, EventSerializer,\
 UserSerializer, CartSerializer, TransactionSerializer, Transaction_infoSerializer, LoginSerializer, RegisterSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView

class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class MusicList(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    pagination_class = BasePagination

class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = BasePagination

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = BasePagination

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #pagination_class = BasePagination

class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Transaction_infoList(generics.ListAPIView):
    queryset = Transaction_info.objects.all()
    serializer_class = Transaction_infoSerializer
    pagination_class = BasePagination

class TransactionList(generics.ListAPIView):
    queryset = Ticket_transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = BasePagination


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer


    def signin(self):
        self.user = self.serializer.validated_data['user']
        login(self.request, self.user)


    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(data={'message':'User was logged on'})
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)
        self.signin()
        return Response(status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Successfully logged out."},status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        username_exists = User.objects.filter(username=username).exists()
        if username_exists:
            return Response({"message": "Username already exists."},status=status.HTTP_400_BAD_REQUEST)
        password=request.POST['password']
        email = request.POST['email']
        password = request.POST['password']
        register = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=username,
                                            email=email,
                                            password=password)
        return Response({"message": "Successfully registered."},status=status.HTTP_200_OK)