from django.shortcuts import render
from music.models import Event, Music, Album, Cart,Ticket_transaction
import json
from django.core.serializers.json import DjangoJSONEncoder
from .data_layer.common import decorators
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm, TransactionForm


def Home(request):
    return render(request,'index.html')

@decorators.ajax_required
def get_json_event(request):
    event_all = Event.objects.all()
    data = []
    for i in event_all:
        data.append(i.get_dict_event())
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

"""{'event':'Green_day','event_for':['Missing_you','Stay The Night'],'location':'Jakarta','price':'500.000'}"""

@decorators.ajax_required
def get_json_music(request):
    music_all = Music.objects.retrieveData()
    data = [i for i in music_all]
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

@decorators.ajax_required
def get_json_album(request):
    album_all = Album.objects.all()
    data = []
    for i in album_all:
        data.append(i.get_dict())
    return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

#untuk tampilkan per album
def Album_view(request,pk):
    obj = Album.objects.only('nameapp','genre','release_date','picture','descriptions').get(idapp=pk)#.values('nameapp','picture','descriptions')
    related_music = obj.music_set.all()
    #data = [i for i in obj]
    template = 'Album_view_render.html'
    if request.is_ajax():
        template = 'Album_view_ajax.html'
    return render(request,template,{'obj':obj,'related_music':related_music})
    #return HttpResponse(json.dumps(data,cls=DjangoJSONEncoder),content_type='application/json')

def Album_list(request):
    album = Album.objects.all()
    data = []
    for i in album:
        data.append(i.get_dict())
    return render(request,'Album_list.html',{'album':data})

from django.contrib.auth.decorators import login_required

@login_required
def Music_list(request, *args, **kwargs):
    music = Music.objects.retrieveData()
    return render(request,'Music_list.html',{'music':music})

def Event_view(request,pk):
    return render(request,'Event_view.html')

def Event_list(request):
    event_all = Event.objects.all()
    event = []
    user = None
    if request.user.is_authenticated:
        user = request.user.id
    for i in event_all:
        event.append(i.get_dict_event(user))
    return render(request,'Event_list.html',{'event':event})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request): # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect(request.GET.get('next'))
    else:
        form = SignInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # authenticates Email & Password
            user = authenticate(username=username, password=password) 
            login(request, user)
            next_action = form.cleaned_data.get('next')
            if next_action is not None:
                return redirect(next_action)
            else :
                return redirect('home')
        else:
            if request.method == 'GET':
                next = request.GET.get('next')
                form.fields['next'].initial = next
                template_name = 'SignIn_render.html'
                if request.is_ajax():
                    template_name = 'SignIn_ajax.html'
                return render(request, template_name, {"form":form})

from oauth2_provider.views.generic import ProtectedResourceView
class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

from django.contrib.auth.models import User
def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return HttpResponse(json.dumps({'username':user.username,'first_name':user.first_name,'password':user.password}),content_type='application/json')

def signout(request): # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logout(request)
        return redirect("home")

def add_cart(request):
    if request.method == 'POST':
        ticket_id = request.POST['ticket']
        username = request.user.username
        user = User.objects.get(username=username)
        ticket = Event.objects.get(idapp=ticket_id)
        cart = Cart.objects.create(ticket=ticket,user=user)
        return HttpResponse(json.dumps({'message':'success','idapp':ticket_id}),content_type='application/json')

def getForm_data(request,form):
    clData = form.cleaned_data
    return {
        'user':User.objects.get(id=request.user.id),
        'ticket':Event.objects.get(idapp=clData['ticket_idapp']),
        'quantity':clData['quantity'],
        'no_telp':clData['no_telp'],
        'province':clData['province'],
        'code_pos':clData['code_pos'],
        'city':clData['city'],
        'address':clData['address']
        }

def GD_Transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            data = getForm_data(request,form)
            Ticket_transaction.objects.create(user=data['user'],ticket=data['ticket'],quantity=data['quantity'],
                                              no_telp=data['no_telp'],province=data['province'],city=data['city'],
                                              address=data['address'])
            return HttpResponse(json.dumps({'message':'success','idapp':data['ticket'].idapp}),content_type='application/json')
    elif request.method == 'GET':
        idapp_ticket = request.GET['idapp']
        form = TransactionForm()
        form.fields['ticket_idapp'].initial = idapp_ticket
        return render(request,'Transaction_form.html',{'form':form})

@login_required
def GD_Cart(request):
    ticket_data = Ticket_transaction.objects.filter(user=request.user.id)
    ticket = [i.get_dict() for i in ticket_data]
    return render(request,'Cart_list.html',{'ticket':ticket})

from django.db.models import F, Sum
def GD_Checkout_list(request):
    ticket_data = Ticket_transaction.objects.filter(user=request.user.id)
    ticket = [i.get_checkout_info() for i in ticket_data]
    return render(request,'Checkout_list.html',{'ticket':ticket})

def GD_Checkout_confirm(request):
    address = Ticket_transaction.objects.filter(user=request.user.id).values('province','city','code_pos','address')
    return render(request,'Checkout_confirm_address.html',{'address':address})