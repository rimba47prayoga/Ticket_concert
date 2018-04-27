from rest_framework import serializers
from music.models import Music,Album, Event, Cart, Ticket_transaction, Transaction_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class MusicSerializer(serializers.ModelSerializer):
    albums = serializers.StringRelatedField(source='album.nameapp')
    class Meta:
        model = Music
        fields = ('nameapp','durations','albums')

class AlbumSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(read_only=True, many=True)
    class Meta:
        model = Album
        fields = ('nameapp','release_date','genre','picture','music_set','descriptions')

class EventSerializer(serializers.ModelSerializer):
    ticket_for = MusicSerializer(read_only=True,many=True)
    ticket_date = serializers.DateTimeField(format="%d %B %Y %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Event
        fields = ('location','ticket_for','ticket_date','price','descriptions')

class UserSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(source='userprofile.picture')
    class Meta:
        model = User
        fields = ('first_name','last_name','picture','username','email','password')

class CartSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(source='user.username')
    ticket = EventSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ('users','ticket')

class Transaction_infoSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(source='user.username')
    createddate = serializers.DateTimeField(format="%d %B %Y %H:%M:%S", required=False, read_only=True)
    modifieddate = serializers.DateTimeField(format="%d %B %Y %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Transaction_info
        fields = ('users','no_telp','province','code_pos','address','createddate','modifieddate')

class TransactionSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(source='user.username')
    ticket = EventSerializer(read_only=True)
    info = Transaction_infoSerializer(read_only=True)
    createddate = serializers.DateTimeField(format="%d %B %Y %H:%M:%S", required=False, read_only=True)
    modifieddate = serializers.DateTimeField(format="%d %B %Y %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Ticket_transaction
        fields = ('users','ticket','info','quantity','total_purchase','createddate','modifieddate')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise ValidationError(msg)
        return user

    def _validate_username(self, username, password):
        user = None
        if username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise ValidationError(msg)
        return user

    def _validate_username_email(self, username, email, password):
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
        elif username and password:
            user = authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        user = None
        if email:
            try:
                username = User.objects.get(email__iexact=email).get_username()
            except User.DoesNotExist:
                pass

        if username:
            user = self._validate_username_email(username, '', password)
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')