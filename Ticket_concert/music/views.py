from django.shortcuts import render
from music.models import Event, Music, Album, Cart,Ticket_transaction, Transaction_info
import json
from django.core.serializers.json import DjangoJSONEncoder
from .data_layer.common import decorators
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from oauth2_provider.views.generic import ProtectedResourceView
from django.contrib.auth.models import User
from django.db.models import F, Sum
from django.db import transaction

from .forms import SignUpForm, SignInForm, Transaction_InfoForm


def Home(request):
    data_album = Album.objects.all()[:5]
    album = [i.get_dict() for i in data_album]
    music = Music.objects.retrieveData()[:4]
    event = Event.objects.all()[:4]
    return render(request,'index.html',{'album':album,
                                        'music':music,
                                        'event':event})

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
    if request.user.is_authenticated:
        return redirect('home')
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
            return HttpResponse('not valid', status=400)
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


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return HttpResponse(json.dumps({'username':user.username,'first_name':user.first_name,'password':user.password}),content_type='application/json')

def signout(request): # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logout(request)
        return redirect("home")

def GD_TransactionInfo_add(request):
    form = Transaction_InfoForm(request.POST)
    if form.is_valid():
        data = getForm_data(request,form)
        print('form valid')
        trans = Transaction_info.objects.create(user=data['user'],
                                            no_telp=data['no_telp'],province=data['province'],city=data['city'],
                                            code_pos=data['code_pos'],address=data['address'])
        return HttpResponse(json.dumps({'message':'success'}),content_type='application/json')

def GD_TransactionInfo(request):
    idapp_ticket = request.GET['idapp']
    form = Transaction_InfoForm()
    context = {}
    transaction_data = Transaction_info.objects.values('idapp','province','city','code_pos','address').filter(user=request.user.id)
    if transaction_data.exists():
        context['transaction_data'] = transaction_data
        form.display = 'none'
    context['form'] = form
    form.fields['ticket_idapp'].initial = idapp_ticket
    return render(request,'Transaction_info_form.html',context)


def GD_Cart_add(request):
    if request.method == 'POST':
        ticket_id = request.POST['ticket_idapp']
        username = request.user.username
        user = User.objects.get(username=username)
        ticket = Event.objects.get(idapp=ticket_id)
        cart = Cart.objects.create(ticket=ticket,user=user,quantity=request.POST['quantity'])
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


@login_required
def GD_Cart(request):
    cart_data = Cart.objects.filter(user=request.user.id)
    cart = [i.get_dict() for i in cart_data]
    return render(request,'Cart_list.html',{'cart':cart})


def GD_Checkout_list(request):
    ticket_data = Cart.objects.filter(user=request.user.id)
    ticket = [i.get_checkout_info() for i in ticket_data]
    return render(request,'Checkout_list.html',{'ticket':ticket})


def GD_Checkout_confirm(request):
    if request.method == 'GET':
        address = Transaction_info.objects.filter(user=request.user.id).values('province','city','code_pos','address')
        return render(request,'Checkout_confirm_address.html',{'address':address})
    elif request.method == 'POST':
        idapp = request.POST['idapp']
        idapp_ticket = request.POST['idapp_ticket']
        quantity = request.POST['quantity']
        with transaction.atomic():
            if ',' in idapp:
                idapp = idapp.split(',')
                idapp_ticket = idapp_ticket.split(',')
                quantity = quantity.split(',')
                for i in range(len(idapp_ticket)):
                    ticket=Event.objects.get(idapp=idapp_ticket[i])
                    ticket.total_ticket = ticket.total_ticket - int(quantity[i])
                    ticket.save()
                    Ticket_transaction.objects.create(user=User.objects.get(id=request.user.id),
                                                      ticket=ticket,
                                                      quantity=quantity[i])
                Cart.objects.filter(idapp__in=idapp).delete()
            else:
                ticket=Event.objects.get(idapp=idapp_ticket)
                ticket.total_ticket = ticket.total_ticket - int(quantity)
                ticket.save()
                Ticket_transaction.objects.create(user=User.objects.get(id=request.user.id),
                                                      ticket=Event.objects.get(idapp=idapp_ticket),
                                                      quantity=quantity)
                Cart.objects.filter(idapp=idapp).delete()
        return HttpResponse(json.dumps({'message':'success','idapp':idapp}),content_type='application/json')
        